from huggingface_hub import snapshot_download

# 替换为目标目录
local_dir = "/mnt/c/Users/user/Desktop/AnimateDiff/models/StableDiffusion/stable-diffusion-v1-5"
snapshot_download(
    repo_id="runwayml/stable-diffusion-v1-5",
    cache_dir=local_dir,
    allow_patterns=["*"],  # 下载所有文件
)

