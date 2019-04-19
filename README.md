# sc2agent
[![Build Status](https://travis-ci.org/AUCR/sc2agent.svg?branch=master)](https://travis-ci.org/sc2agent/sc2agent)
[![codecov](https://codecov.io/gh/AUCR/sc2agent/branch/master/graph/badge.svg)](https://codecov.io/gh/sc2agent/sc2agent)
[![Docker Repository on Quay](https://quay.io/repository/wroersma/sc2agent/status "Docker Repository on Quay")](https://quay.io/repository/wroersma/sc2agent)
[![Coverage Status](https://coveralls.io/repos/github/AUCR/sc2agent/badge.svg)](https://coveralls.io/github/sc2agent/sc2agent)
[![Code Health](https://landscape.io/github/AUCR/sc2agent/master/landscape.svg?style=flat)](https://landscape.io/github/sc2agent/sc2agent/master)
[![sc2agent Slack](https://slack.sc2agent.io/badge.svg)](https://slack.aucr.io/)


## Overview

The goal of sc2agent is provide a simple python app(at some point I plan to finish the go version) that submits replays to various services.
Currently it only supports submitting replays to the starcraft_plugin for AUCR.

## How to setup
This app requires Python >= 3.7  

    pip install -r requiremnets.txt
    python setup.py install
    export API_URL=https://sc2agent.aucr.io
    export API_KEY=your-account-api-key-here
    export REPLAY_FILE_PATH="C:\\Users\your-username-here\\Documents\\StarCraft II\\Accounts\account-id\\account-sid\\Replays\\Multiplayer"
    sc2agent_cli.py 

    
## Easy Docker use

    copy config-file-example.env config-file.env
    open config-file.env in a text editor and replace with your API_KEY
    docker-compose up -d


### Required Services

- AUCR running with starcraft_plugin 


## Example: Environment Variables

        LC_ALL=C.UTF-8
        LANG=C.UTF-8
        API_URL=https://sc2agent.aucr.io
        API_KEY=your-account-api-key-here
        REPLAY_FILE_PATH="C:\\Users\your-username-here\\Documents\\StarCraft II\\Accounts\account-id\\account-sid\\Replays\\Multiplayer"
 
