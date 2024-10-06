# boole

Uma linguagem para Álgebra Booleana

# Install from source

Clone o repositório:

``` git clone https://github.com/pab-h/boole```

# How run a boole program?

Para compilar um programa escrito em boole, você só precisa ter o [python](https://www.python.org/downloads/)

Na raiz do projeto,

```bash
python main.py [source] --execute
```
Tente executar os **exemplos**:
```bash
python main.py examples/1.bool --execute
python main.py examples/2.bool --execute
python main.py examples/3.bool --execute
```

> Serão gerandos códigos python dentro da pasta *bin*

# Docs

## Operators

Os seguintes operadores booleanos foram implementados:

| Operator | Description |
| --- | --- |
| * | AND  |
| + | OR |
| ^ | XOR |
| ! | NOT |
| -> | IF |
| <-> | IF AND ONLY IF |

Além disso, 

| Operator | Description |
| --- | --- |
| > | PRINT*  |
| := | ASSING |

*Só pode ser usado no início de uma declaração

## Variables

```python
[IDENTIFIER] := [BIT]
```
```python
A := 0
B := 1
```
## Functions

```python
fn [IDENTIFIER]([PARAMS]) := [BODY]
```
```python
fn z(A, B) := !A * B ^ (A * B)
fn g(A, B) := A ^ B
fn h(A, B, C) := g(A, z(B, C))

> z(0, 1)
> h(0, 1, 1)
```

### Built-in Functions

| Operator | Description |
| --- | --- |
| table(.) | Mostra a tabela verdade da função  |
| graph(z) | Mostra o gráfico de linha dessa função |
| graph(z, ...) | Mostra o gráfico de linha dessa função dados os sinais passados |

```python
fn z(A, B, C) := A * B * C

table(z)

graph(z)

a[] := [0, 1, 1, 1, 0, 1]
b[] := [0, 1, 1, 1, 0, 1]
c[] := [0, 1, 1, 1, 0, 1]

graph(z, a, b, c)
```

# The future
- [ ] Impressão de funções;
- [x] Mais funções embutidas: minterm, maxterm, minimize, clock;
