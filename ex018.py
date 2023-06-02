#Exercício do angulo da tangente
from math import radians, cos, sin, tan
ângulo = float(input(('Qual o ângulo que você deseja? ')))
seno = sin(radians(ângulo))
cos = cos(radians(ângulo))
tan = tan(radians(ângulo))
print(f'O ângulo de {ângulo}º tem o seno de {seno:.2f}')
print(f'O ângulo de {ângulo}º tem o cosseno de {cos:.2f}')
print(f'E o ângulo de {ângulo}º tem a tengente de {tan:.2f}')