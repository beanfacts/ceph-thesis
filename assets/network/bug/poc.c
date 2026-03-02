struct ibv_ah * ah = ibv_create_ah(pd, &ah_attr);
if (!ah)
    return EXIT_FAILURE;

struct ibv_mr * mrs[5];
struct ibv_sge  sges[5];
void          * bufs[5];

for (int i = 0; i < 5; i++) {
    bufs[i]        = alloc_aligned_mr(1, &mrs[i], pd, 0);
    sges[i].addr   = (uintptr_t) bufs[i];
    sges[i].length = 1;
    sges[i].lkey   = mrs[i]->lkey;
}

struct ibv_send_wr wr = {
    .wr_id      = 0xdead, .sg_list    = sges,
    .num_sge    = 5,      .opcode     = IBV_WR_SEND,
    .send_flags = 0,      
    .wr = {
        .ud = {
            .ah = ah,
            .remote_qpn = qp->qp_num,
            .remote_qkey = 0x11111111,
        },
    }
};