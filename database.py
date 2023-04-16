from replit import db

# db["vid_one"] = {
#   "link": "www.youtube.com/watch?v=0DPZ9b9ZZr4",
#   "id": 0,
#   "caption": "Video of dogs doing cute and funny things",
#   "name": "Cute Dog Complimation"
# }

# db["vid_two"] = {
#   "link": "www.youtube.com/watch?v=Sg4hFC9rrzI",
#   "id": 1,
#   "caption": "Silly cats and dogs",
#   "name": "Cat and Dogs Video"
# }
# db["vid_three"] = {
#   "link": "https://www.youtube.com/embed/PDj0gR_xsYE",
#   "id": 0,
#   "caption": "Proof that German Shepards are fantastic dogs",
#   "name": "German Shepards"
# }
for e in db:
  print(e)
