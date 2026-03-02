def parse_mdtest_result(
    nodes: int, ppn: int, cmdline: str, began: datetime, finished: datetime, 
    mdtest_output: str,
) -> MDTestOutput:
    def _opt(t, row: dict, key: str) -> Optional[Any]:
        try:
            return t(row[key])
        except (TypeError, ValueError, KeyError):
            return None

    def _gen_mdtest_stats(row: dict, pfx: str) -> MDTestStats:
        return MDTestStats(
            create_rate=_opt(float, row, f"rate-{pfx} creation"),
            create_time=_opt(float, row, f"time-{pfx} creation"),
            stat_rate=_opt(float, row, f"rate-{pfx} stat"),
            stat_time=_opt(float, row, f"time-{pfx} stat"),
            read_rate=_opt(float, row, f"rate-{pfx} read"),
            read_time=_opt(float, row, f"time-{pfx} read"),
            rename_rate=_opt(float, row, f"rate-{pfx} rename"),
            rename_time=_opt(float, row, f"time-{pfx} rename"),
            remove_rate=_opt(float, row, f"rate-{pfx} removal"),
            remove_time=_opt(float, row, f"time-{pfx} removal"),
        )

    reader = csv.DictReader(mdtest_output.splitlines())
    results = []
    for row in reader:
        detail = MDTestResultDetail(
            rank=_opt(int, row, "rank") or -1,
            items=_opt(int, row, "items") or 0,
            dir_stats=_gen_mdtest_stats(row, "Directory"),
            file_stats=_gen_mdtest_stats(row, "File"),
            tree_stats=_gen_mdtest_stats(row, "Tree"),
        )
        results.append(detail)

    return MDTestOutput(
        nodes=nodes, tasks_per_node=ppn, total_tasks=nodes * ppn,
        command_line=cmdline, began=began, finished=finished,
        results=results,
    )