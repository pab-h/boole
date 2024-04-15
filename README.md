# boole
Um interpretador para a álgebra booleana

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

# The Sintaxe

A sintaxa aceita pela linguagem boole é compilada como segue:

```
program: statementList
statementList: statement{statement 'BREAKLINE'}
statement: declarationStatement | assignmentStatement | empty
declarationStatement: type assignmentStatement
assignmentStatement: variable 'ASSIGN' expr
variable: 'IDENTIFIER'
empty: 
type: 'BIT'
expr: term{'AND' term}
term: factor{'AND' factor}
factor: 'LITERALBIT'('LEFTBRACKET' expr 'RIGHTBRACKET') | 'NOT' factor
```


# Operators

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

# Variable Declaration

Segue o padrão da maioria das linguagens tipadas: 
` bit <id> = <value>`

Para ver o valor das variáveis, basta digitar "_".

```
In[0] > bit a = 0
Out[0] > None

In[1] > bit b = 1
Out[1] > None

In[2] > bit c = a * b
Out[2] > None

In[3] > _
{'a': False, 'b': True, 'c': False}
```

# Scripts

```poetry run idle``` -> Inicializa o idle

```poetry run test``` -> Executa os testes unitários
