segundos = int(input('Por favor, entre com o número de segundos que deseja converter: '))

contdia = segundos // 86400
restdia = (segundos % 86400)
conthora = restdia // 3600
resthora = (restdia%3600)
contmin = resthora//60
restmin = (resthora%60)
contseg = restmin//60
seg = restmin%60


print(contdia,'dias,',conthora,'horas,',contmin,'minutos,',seg,'segundos.')


