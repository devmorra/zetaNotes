## SELECT statement
* To see a subset of rows, columns, or both
* Result of the query is called a result set, lists rows that contain the same number of columns
* SELECT column_2 column_3 column_4 FROM table_employees
![](SELECT%20example.jpg)


## Optional clauses
* WHERE - where certain rows contain a specified value
* GROUP BY - Request only certain rows from a table
* HAVING - Use a column identifier to organize the data in the result set into groups Use in conjunction with GROUP BY to specify which groups to include in results
* ORDER BY - Sort query results by one or more columns and in ascending or descending order 
Square brackets indicate optional parameters, * is used as a wildcard (all columns)

## SQL statement guidelines
Separate words with at least once space or line break.
Keywords can be uppercase or lowercase.  
Limit table column and index names so that they 
1. Always start with a letter
2. Are under 30 characters
3. Don't have spaces  

Use case sensitivity just in case (since it depends on the SQL implementation). Use single quotes to keep track of strings literally.

-- to comment, can be a standalone line or after a line  
/* and */ for multi-line comments

## Conditional searches
Use the previously mentioned optional clauses  
Process goes like: query > search for records > retrieve records > display records

Clauses can include arithmetic, comparator, and logical operators (ex. +, -, * >, <=, OR, AND, NOT, etc.)

Arithmetic operators can also be applied to data that's being returned (ex. take temperature value and convert to F or C with a forumla)

## Aliasing
SELECT (columns + calculation) AS alias
Creates a new column with the specified calculation with the title of the given alias
![](Alias%20examples.jpg)  
AS keyword is optional. Can use single quotes to create a column name with spaces

## Logical operators
ALL - TRUE if all following conditions must be met  
AND - TRUE if both sides are TRUE  
ANY - TRUE if any of the following conditions can be met  
BETWEEN - TRUE if the operand is within a given range  
EXISTS - TRUE if a subquery contains any rows  
IN - TRUE if the operand is equal to a given list of expressions (similar to a for loop) Specify list with (), delimit with commas  
LIKE - TRUE if the operand matches a pattern  
OR - TRUE if either side is TRUE  
SOME - TRUE if some of a set of comparisons are TRUE (how is this different from ANY?)  
NOT - Inverts the logic TRUE <-> FALSE  
![](Operator%20precedence.jpg)  
Parenthesis can group logic together similarly to arithmetic, overriding the above.

## NULL
TRUE AND NULL = FALSE
TRUE OR NULL = TRUE
NULL AND NULL = FALSE
NULL OR NULL = UNKNOWN
FALSE AND NULL = FALSE
FALSE OR NULL = UNKNOWN

NULL does not equal NULL. IS NULL returns TRUE if the value is NULL.

## [Wildcards](https://www.w3schools.com/sql/sql_wildcards.asp)
Used with LIKE operator. 
'%hello%' returns entries that contain 'hello' anywhere in them 
Upperof/Lowerof - functions that convert what's inside their following parentheses  
Can use REGEXP keyword to use regular expression

# Functions
Just like functions in other languages. FUNCTION_NAME(parameter1, parameter2)  
Can nest functions like other languages.  

## Aggregate Functions
Self explanatory in terms of what they do.
COUNT  
AVG  
SUM  
MIN  
MAX  
![](Aggregate%20example.jpg)  
^Example of usage. Note how they save their value to a variable given after they're called.

Put a keyword in double quotes to use it outside its context

DISTINCT keyword prevents duplicate row values

## Strings
Enclosed in single quotes. Cannot be used with arithmetic as expected. String functions include:  
LEN(str), UPPER(str), LOWER(str)  
LTRIM(str) & RTRIM(str) remove whitespace from the left and right sides respectively  
SUBSTRING(str,start,stop)  
CONCAT(str,str,str,...), looks like it can be used with other data types as well as long as they match. Can put in literal strings as well as variables
