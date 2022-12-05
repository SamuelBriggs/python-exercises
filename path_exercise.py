from pathlib import Path

fake_path = Path("c:\cohort14")

cwd_path = Path.cwd() / "felix"
cwd_path.mkdir(exist_ok=True)

print(cwd_path)

print(Path.cwd())
print(cwd_path.exists())

