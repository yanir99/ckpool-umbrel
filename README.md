# CKPool Solo Umbrel App

A custom Umbrel app to run the [pinkyswear/ckpool-solo](https://hub.docker.com/r/pinkyswear/ckpool-solo) solo mining pool with:

- Config editor via web UI (filebrowser port 5008)
- Log viewer
- Stratum port (5333) exposed
- Manual integration with Umbrel's Bitcoin Core node

## Features

- Edit `ckpool.conf` directly in the web UI
- View `/logs` and its subfolders
- Customize mining addresses, donations, and ZMQ

## Setup (Umbrel)

Add this repo as a community app store
   https://github.com/yanir99/umbrel-ckpool
