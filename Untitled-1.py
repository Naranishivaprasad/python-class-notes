movie_info={'moviename': 'kingdom', 
 'budget': '70cr', 
 'release-date': '31/07/2025', 
 'director': 'gautham', 
 'genre': 'action', 
 'cast': ['VD', 'SD', 'BHAGAYASRI'], 
 'remuneration': {'vd_rem': '25cr', 'sd_rem': '5cr', 'bhagi_rem': '2cr'} }

 

print(f"{movie_info['cast'][0]} is charging {movie_info['remuneration']['vd_rem']} for acting in {movie_info['moviename'] } movie")

del movie_info['genre']
print(movie_info)
movie_name=["kingdom",'hhvm','coolie','war2','hit3']
print(movie_name[len(movie_name)-1])
op=movie_name+['ms.dhoni']
print(op)




