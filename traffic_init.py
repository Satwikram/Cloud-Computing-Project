def __init__(self, config={}):
  
  self.set_default_config()

  for attr, val in config.items():
      setattr(self, attr, val)