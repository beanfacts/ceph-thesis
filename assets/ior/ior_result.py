class IORResult(BaseModel):
    access: AccessType
    bw_bytes: float = Field(alias="bwMiB")  # converted
    block_bytes: Union[int, float] = Field(alias="blockKiB")  # converted
    xfer_bytes: Union[int, float] = Field(alias="xferKiB")  # converted
    iops: float
    latency: float
    open_time: float = Field(alias="openTime")
    wr_rd_time: float = Field(alias="wrRdTime")
    close_time: float = Field(alias="closeTime")
    total_time: float = Field(alias="totalTime")