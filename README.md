# CKPool Solo Umbrel App

A custom Umbrel app to run the [pinkyswear/ckpool-solo](https://hub.docker.com/r/pinkyswear/ckpool-solo) solo mining pool with:

- Config editor via web UI
- Log viewer
- Stratum port (3333) exposed
- Optional integration with Umbrel's Bitcoin Core node

## Features

- Edit `ckpool.conf` directly in the web UI
- View `/logs` and its subfolders
- Customize mining addresses, donations, and ZMQ

## Setup (Umbrel)

1. Clone this repo into your Umbrel apps directory:
   ```bash
   git clone https://github.com/yanir99/ckpool-umbrel ~/umbrel/apps/ckpool-umbrel
