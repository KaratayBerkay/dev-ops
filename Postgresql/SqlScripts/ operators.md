## Operator Precedence 

 The precedence and associativity of the operators is hard-wired into the parser. Add parentheses if you want an 
 expression with multiple operators to be parsed in some other way than what the precedence rules imply.

| Operator/Element              | Interpretation | Description                                        |
|-------------------------------|----------------|----------------------------------------------------|
| .                             | left           | table/column name separator                        |
| ::                            | left           | PostgreSQL-style typecast                          |
| [ ]                           | left           | array element selection                            |
| + -                           | right          | unary plus, unary minus                            |
| ^                             | left           | exponentiation                                     |
| * / %                         | left           | multiplication, division, modulo                   |
| + -                           | left           | addition, subtraction                              |
| (any other operator)          | left           | all other native and user-defined operators        |
| BETWEEN IN LIKE ILIKE SIMILAR |                | range containment, set membership, string matching |
| < > = <= >= <>                |                | comparison operators                               |
| IS ISNULL NOTNULL             |                | IS TRUE, IS FALSE, IS NULL, IS DISTINCT FROM, etc. |
| NOT                           | right          | addition, subtraction                              |
| AND                           | left           | addition, subtraction                              |
| OR                            | left           | addition, subtraction                              |

```shell
SELECT 3 OPERATOR(pg_catalog.+) 4;
```
