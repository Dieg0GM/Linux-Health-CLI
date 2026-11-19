# Docker quickstart

This is an educational container. Docker must be available locally or inside your Codespace.

```bash
docker build -t linux-health-cli .
docker run --rm linux-health-cli
```

Run tests first with `python3 -m unittest discover -s tests -v`. The CI workflow builds this image automatically after tests pass. Do not put secrets into images.
