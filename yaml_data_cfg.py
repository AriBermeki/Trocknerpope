import yaml
with open('cfg.yaml') as ari:
    data = yaml.load(ari, Loader=yaml.FullLoader)
    sequenz = data['DATABASE_URI']
   