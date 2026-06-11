# Problem Zero 

## Code Implementation
* [problem_zero.py](../problems/problem_zero.py)
* [problem_zero_test.py](../tests/problem_zero/problem_zero_test.py)
    * [square_numbers.tx](../tests/problem_zero/square_numbers.txt)

## Architecture & Flow

### `is_square_number` Flow  
```mermaid
flowchart TD
    A["Input: num"] --> B{"num <= 1?"}
    B -->|Yes| C["Return []"]
    B -->|No| D{"num % divisor == 0?"}
    D -->|Yes| E["Prepend divisor<br/>Recurse: num//divisor"]
    D -->|No| F["Recurse: num<br/>divisor + 1"]
    E --> G["Return list"]
    F --> G
    C --> H["Check prime factors"]
    G --> I["Count factor frequencies"]
    I --> J{"All frequencies<br/>even?"}
    J -->|Yes| K["Return True<br/>is_square_num"]
    J -->|No| L["Return False<br/>not_square_num"]
```

### Modules Architecture Class Diagram
```mermaid
classDiagram
    class problem_zero {
        -max_count: int
        -square_nums: list
        +get_prime_factors(num: int, divisor: int = 2) list
        +is_square_num(num: int) bool
        +main()
    }
    
    class problem_zero_test {
        +test_is_squares_number_should_validate_a_valid_square_number_correctly()
        +test_is_squares_number_should_validate_non_square_numbers_correctly()
        +test_is_squares_number_should_validate_one_as_valid_square_number()
        +test_is_squares_number_should_validate_valid_square_numbers()
        +test_get_prime_factors_should_return_valid_factors()
        +test_get_prime_factors_should_return_empty_list_for_one()
    }
    
    problem_zero_test --> problem_zero : imports & tests
```