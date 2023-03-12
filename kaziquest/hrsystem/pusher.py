import pusher

pusher_client = pusher.Pusher(
  app_id='1566885',
  key='bf47d2ee849e58d4a6f3',
  secret='323aa920f70e2d327b9c',
  cluster='ap2',
  ssl=True
)

# pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})