### README

# Karting Bot Project

This project uses https://timing.batyrshin.name to collect and update information on the best karting karts by best times over 1, 7 and 14 days.

## Installation and Setup


### Guide

1. **Clone the repository:**

2. **Set up your environment:**

   - **Edit `parsi4.py` and `boti4.py` to include your Telegram bot token.**

   - **Set up `run.sh` with the base path to your project and the desired interval `N` in minutes:**

3. **Run the script:**
   ```bash
   bash run.sh
   ```

## Usage

- The script will set up a cron job to run the parser and updater at the specified interval.
- The bot will be started immediately after setting up the cron job.

