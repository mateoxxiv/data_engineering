## downstream

```bash
# operacion 1
tarea1.set_downstream(tarea2)
tarea2.set_downstream([tarea3, tarea4])
```

## bitshift operators

```bash
tarea1 >> tarea2 >> [tarea3, tarea4]
```

## upstream

```bash
# operacion 1
tarea1.set_upstream(tarea2)
tarea2.set_upstream([tarea3, tarea4])
```

## bitshift operators

```bash
tarea1 << tarea2 << [tarea3, tarea4]
```