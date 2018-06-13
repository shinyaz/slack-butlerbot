# butlerbot
A chat bot for [Slack](https://slack.com) based on [slackbot](https://github.com/lins05/slackbot).

## How to Build
```
cp slackbot_settings.py.sample slackbot_settings.py

# Update API and Room
vi slackbot_settings.py

docker build -t butler .
```

## How to Run
```
docker run -d --name=butlerbot --restart=always butlerbot
```

## Acknowledgements

Inspiration and code was taken from many sources, including:
* [@pyconjp](https://github.com/pyconjp) (PyCon JP)
  [https://github.com/pyconjp/pyconjpbot](https://github.com/pyconjp/pyconjpbot)
