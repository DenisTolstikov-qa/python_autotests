import requests

token = '07e176baf984976832eb2ea7e7759a7f'
response = requests.post('https://pokemonbattle.me:9104/trainers/reg', headers = {'Content-Type' : 'application/json'}, 
                         json = {'trainer_token' : token,'email': 'ivanychd@mail.ru', 'password': 'Iloveqa4' })

print(response.text)

response_confirm = requests.post('https://pokemonbattle.me:9104/trainers/confirm_email', headers = {'Conter-Tape' : 'application/json'},
                                 json = {'trainer_token' : token})

print(response_confirm.text)

add_pokemon_response = requests.post('https://pokemonbattle.me:9104/pokemons', 
                                     headers = {'Conter-Tape' : 'application/json','trainer_token' : token},
                                                    json = {'name': 'Жорик' , 'photo': 'https://dolnikov.ru/pokemons/albums/001.png'} )

print(add_pokemon_response.text)

change_name_response = requests.put('https://pokemonbattle.me:9104/pokemons', 
                                    headers = {'Conter-Tape' : 'application/json','trainer_token' : token},
                                    json = {'pokemon_id': '12327','name': 'Джорж', 'photo': 'https://dolnikov.ru/pokemons/albums/744.png'})

print(change_name_response.text)

catch_pokemon_response =requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball',
                                      headers = {'Conter-Tape' : 'application/json','trainer_token' : token},
                                      json = {'pokemon_id': '12328'})

print(catch_pokemon_response.text)

if add_pokemon_response.status_code == 201:
    print('ok')
else:
    print('not ok')
