# Access Control List(windows)
Commands:
- group --operation [add|delete] [name]
- delete_user [name]
- add_user [name]
- user_oper_group --operation [add|delete] [group_name] [user_name]
- admin_oper --operation [add|delete] [name]
- create_folder --mode [R|W|D, RWD] --sid [1-0|3-0|5-11|5-32-544|5-32-545] [path]
- check_perm [path]
## Example:
```
python cli.py create_folder --mode RW --sid 5-32-545 petux4
```
```
python cli.py group --operation add iit1
```
