from pathlib import Path

from modelscope import snapshot_download


MODEL_ID = "BAAI/bge-m3"
TARGET_DIR = Path(r"C:\maxkb\model\local_embedding\bge-m3")


def main() -> None:
    TARGET_DIR.mkdir(parents=True, exist_ok=True)

    model_dir = snapshot_download(
        model_id=MODEL_ID,
        local_dir=str(TARGET_DIR),
    )

    print(f"Model downloaded to: {model_dir}")
    print("Use this path in MaxKB:")
    print("/opt/maxkb/model/local_embedding/bge-m3")


if __name__ == "__main__":
    main()
