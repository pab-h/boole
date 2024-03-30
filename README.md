# boole
A interpreter for Boolean Algebra

# Install from source

Nesse processo, é necessário utilizar a ferramenta [poetry](https://python-poetry.org/). 

Clone o repositório:

``` git clone https://github.com/pab-h/boole```

Instale corretamente as dependência do projeto usando o **poetry**:

``` poetry install``` 

Após instalado as dependências,  utilize o seguinte comando para iniciar o IDLE (Integrated Development and Learning Environment):

``` poetry run idle``` 

# The Idle

Idle é um ambiente de desenvolvimento integrado para a linguagem Boole. Você pode escrever sentenças válidas para seus testes. Divirta-se.

Para iniciar o Idle, basta executar:

``` poetry run idle``` 

Para sair do idle, basta escrever:

``` exit``` 


# Operadores

## AND
```
In[0] > 1*0
Out[0] > False

In[1] > 1&1
Out[1] > True
```

## OR
```
In[0] > 1+0
Out[0] > True

In[1] > 1|1
Out[1] > True
```

## NOT
```
In[0] > !0
Out[0] > True

In[1] > !1 
Out[1] > False

In[2] > !!0
Out[2] > False

In[3] > ~1
Out[3] > False
```

# The Sintaxe

A sintaxa aceita pela linguagem boole é compilada como segue:

```
expr: term{'AND' term}
term: factor{'AND' factor}
factor: LOGIC('LEFTBRACKET' expr 'RIGHTBRACKET') | 'NOT' factor
```

# Scripts

```poetry run idle``` -> Inicializa o idle

```poetry run test``` -> Executa os testes unitários
