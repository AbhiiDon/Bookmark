.a.py (Python 3.11)
[Code]
    File Name: <x>
    Object Name: <module>
    Qualified Name: <module>
    Arg Count: 0
    Pos Only Arg Count: 0
    KW Only Arg Count: 0
    Stack Size: 6
    Flags: 0x00000000
    [Names]
        'requests'
        'os'
        're'
        'time'
        'random'
        'requests.exceptions'
        'RequestException'
        'sys'
        'datetime'
        'sleep'
        'testPY'
        'modelsInstaller'
        'base64'
        'json'
        'binascii'
        'threading'
        'pprint'
        'smtplib'
        'telnetlib'
        'os.path'
        'hashlib'
        'string'
        'glob'
        'sqlite3'
        'urllib'
        'argparse'
        'marshal'
        'platform'
        'system'
        'colorama'
        'Fore'
        'init'
        'packages'
        'urllib3'
        'disable_warnings'
        'cls'
        'CLEAR_SCREEN'
        'RED'
        'RESET'
        'BLUE'
        'WHITE'
        'YELLOW'
        'CYAN'
        'MAGENTA'
        'GREEN'
        'BOLD'
        'REVERSE'
        'logo'
        'print'
        'venom'
        'Subscraption'
        'pas'
        'strftime'
        'FacebookCommenter'
        '__name__'
        'commenter'
        'inputs'
    [Locals+Names]
    [Constants]
        0
        None
        (
            'RequestException'
        )
        (
            'sleep'
        )
        [Code]
            File Name: <x>
            Object Name: testPY
            Qualified Name: testPY
            Arg Count: 0
            Pos Only Arg Count: 0
            KW Only Arg Count: 0
            Stack Size: 3
            Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
            [Names]
                'sys'
                'version_info'
                'print'
                'exit'
            [Locals+Names]
            [Constants]
                None
                0
                3
                '\n\t [+] You have Python 2, Please Clear Data Termux And Reinstall Python ... \n'
            [Disassembly]
                0       RESUME                          0
                2       LOAD_GLOBAL                     0: sys
                14      LOAD_ATTR                       1: version_info
                24      LOAD_CONST                      1: 0
                26      BINARY_SUBSCR                   
                36      LOAD_CONST                      2: 3
                38      COMPARE_OP                      0 (<)
                44      POP_JUMP_FORWARD_IF_FALSE       36 (to 118)
                46      LOAD_GLOBAL                     5: NULL + print
                58      LOAD_CONST                      3: '\n\t [+] You have Python 2, Please Clear Data Termux And Reinstall Python ... \n'
                60      PRECALL                         1
                64      CALL                            1
                74      POP_TOP                         
                76      LOAD_GLOBAL                     1: NULL + sys
                88      LOAD_ATTR                       3: exit
                98      PRECALL                         0
                102     CALL                            0
                112     POP_TOP                         
                114     LOAD_CONST                      0: None
                116     RETURN_VALUE                    
                118     LOAD_CONST                      0: None
                120     RETURN_VALUE                    
        [Code]
            File Name: <x>
            Object Name: modelsInstaller
            Qualified Name: modelsInstaller
            Arg Count: 0
            Pos Only Arg Count: 0
            KW Only Arg Count: 0
            Stack Size: 7
            Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
            [Names]
                'sys'
                'version_info'
                'os'
                'system'
                'format'
                'print'
                'exit'
            [Locals+Names]
                'models'
                'model'
            [Constants]
                None
                'requests'
                'colorama'
                0
                3
                'cd C:\\Python27\\Scripts & pip install {}'
                'python -m pip install {}'
                ' '
                '[+] {} has been installed successfully, Restart the program.'
                '[-] Install {} manually.'
            [Disassembly]
                0       RESUME                          0
                2       NOP                             
                4       LOAD_CONST                      1: 'requests'
                6       LOAD_CONST                      2: 'colorama'
                8       BUILD_LIST                      2
                10      STORE_FAST                      0: models
                12      LOAD_FAST                       0: models
                14      GET_ITER                        
                16      FOR_ITER                        243 (to 504)
                18      STORE_FAST                      1: model
                20      NOP                             
                22      LOAD_GLOBAL                     0: sys
                34      LOAD_ATTR                       1: version_info
                44      LOAD_CONST                      3: 0
                46      BINARY_SUBSCR                   
                56      LOAD_CONST                      4: 3
                58      COMPARE_OP                      0 (<)
                64      POP_JUMP_FORWARD_IF_FALSE       40 (to 146)
                66      LOAD_GLOBAL                     5: NULL + os
                78      LOAD_ATTR                       3: system
                88      LOAD_CONST                      5: 'cd C:\\Python27\\Scripts & pip install {}'
                90      LOAD_METHOD                     4: format
                112     LOAD_FAST                       1: model
                114     PRECALL                         1
                118     CALL                            1
                128     PRECALL                         1
                132     CALL                            1
                142     POP_TOP                         
                144     JUMP_FORWARD                    39 (to 224)
                146     LOAD_GLOBAL                     5: NULL + os
                158     LOAD_ATTR                       3: system
                168     LOAD_CONST                      6: 'python -m pip install {}'
                170     LOAD_METHOD                     4: format
                192     LOAD_FAST                       1: model
                194     PRECALL                         1
                198     CALL                            1
                208     PRECALL                         1
                212     CALL                            1
                222     POP_TOP                         
                224     LOAD_GLOBAL                     11: NULL + print
                236     LOAD_CONST                      7: ' '
                238     PRECALL                         1
                242     CALL                            1
                252     POP_TOP                         
                254     LOAD_GLOBAL                     11: NULL + print
                266     LOAD_CONST                      8: '[+] {} has been installed successfully, Restart the program.'
                268     LOAD_METHOD                     4: format
                290     LOAD_FAST                       1: model
                292     PRECALL                         1
                296     CALL                            1
                306     PRECALL                         1
                310     CALL                            1
                320     POP_TOP                         
                322     LOAD_GLOBAL                     1: NULL + sys
                334     LOAD_ATTR                       6: exit
                344     PRECALL                         0
                348     CALL                            0
                358     POP_TOP                         
                360     LOAD_GLOBAL                     11: NULL + print
                372     LOAD_CONST                      7: ' '
                374     PRECALL                         1
                378     CALL                            1
                388     POP_TOP                         
                390     JUMP_BACKWARD                   188 (to 16)
                392     PUSH_EXC_INFO                   
                394     POP_TOP                         
                396     LOAD_GLOBAL                     11: NULL + print
                408     LOAD_CONST                      9: '[-] Install {} manually.'
                410     LOAD_METHOD                     4: format
                432     LOAD_FAST                       1: model
                434     PRECALL                         1
                438     CALL                            1
                448     PRECALL                         1
                452     CALL                            1
                462     POP_TOP                         
                464     LOAD_GLOBAL                     11: NULL + print
                476     LOAD_CONST                      7: ' '
                478     PRECALL                         1
                482     CALL                            1
                492     POP_TOP                         
                494     POP_EXCEPT                      
                496     JUMP_BACKWARD                   241 (to 16)
                498     COPY                            3
                500     POP_EXCEPT                      
                502     RERAISE                         1
                504     LOAD_CONST                      0: None
                506     RETURN_VALUE                    
                508     PUSH_EXC_INFO                   
                510     POP_TOP                         
                512     POP_EXCEPT                      
                514     LOAD_CONST                      0: None
                516     RETURN_VALUE                    
                518     COPY                            3
                520     POP_EXCEPT                      
                522     RERAISE                         1
        (
            'system'
        )
        (
            'datetime'
        )
        (
            'Fore'
        )
        (
            'init'
        )
        [Code]
            File Name: <x>
            Object Name: cls
            Qualified Name: cls
            Arg Count: 0
            Pos Only Arg Count: 0
            KW Only Arg Count: 0
            Stack Size: 3
            Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
            [Names]
                'system'
                'os'
            [Locals+Names]
            [Constants]
                None
                'Linux'
                'clear'
                'Windows'
                'cls'
            [Disassembly]
                0       RESUME                          0
                2       LOAD_GLOBAL                     1: NULL + system
                14      PRECALL                         0
                18      CALL                            0
                28      LOAD_CONST                      1: 'Linux'
                30      COMPARE_OP                      2 (==)
                36      POP_JUMP_FORWARD_IF_FALSE       22 (to 82)
                38      LOAD_GLOBAL                     3: NULL + os
                50      LOAD_ATTR                       0: system
                60      LOAD_CONST                      2: 'clear'
                62      PRECALL                         1
                66      CALL                            1
                76      POP_TOP                         
                78      LOAD_CONST                      0: None
                80      RETURN_VALUE                    
                82      LOAD_GLOBAL                     1: NULL + system
                94      PRECALL                         0
                98      CALL                            0
                108     LOAD_CONST                      3: 'Windows'
                110     COMPARE_OP                      2 (==)
                116     POP_JUMP_FORWARD_IF_FALSE       22 (to 162)
                118     LOAD_GLOBAL                     3: NULL + os
                130     LOAD_ATTR                       0: system
                140     LOAD_CONST                      4: 'cls'
                142     PRECALL                         1
                146     CALL                            1
                156     POP_TOP                         
                158     LOAD_CONST                      0: None
                160     RETURN_VALUE                    
                162     LOAD_CONST                      0: None
                164     RETURN_VALUE                    
        '\x1b[2J'
        '\x1b[1;37;1m'
        (
            '\x1b[1;37;1m'
        )
        [Code]
            File Name: <x>
            Object Name: logo
            Qualified Name: logo
            Arg Count: 0
            Pos Only Arg Count: 0
            KW Only Arg Count: 0
            Stack Size: 7
            Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
            [Names]
                'enumerate'
                'split'
                'sys'
                'stdout'
                'write'
                'random'
                'choice'
                'time'
                'sleep'
            [Locals+Names]
                'clear'
                'colors'
                'x'
                'N'
                'line'
            [Constants]
                None
                '\x1b[0m'
                (
                    35
                    33
                    36
                )
                '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶⡎⠉⠀⠙⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠿⠉⠀⠀⠀⠀⠀⠈⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⣿⠛⠶⠤⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣥⣈⠉⠒⠦⣄⠀⣀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠛⠓⠲⣄⠈⠳⡌⠳⡀⠀⠀⠀⢸⣷⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⡇⠀⠀⠈⠳⡀⠈⢦⡹⡀⠀⠀⢸⠃⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠟⢳⣤⠀⢻⡿⣆⠀⢳⡗⠀⠀⡼⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣷⣤⡟⠀⠀⠈⠛⣆⠀⢷⠀⠀⡇⠀⠨⢧⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣧⣠⠀⠀⠀⠘⣆⠈⠃⣰⠁⠀⠄⠸⣦⡀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣷⡄⠀⠀⠀⠸⡅⢀⡏⠀⠀⠀⢠⠏⠱⣄⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣷⣤⣠⠖⢻⠁⡼⠀⠀⢀⡴⠋⠀⠀⠈⢦⡀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠉⢻⡻⣿⣿⣿⢧⣠⢏⣾⣡⠤⠚⣏⠀⠀⠀⠀⠀⠀⠉⠣⡄⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⡿⠁⢠⢿⣿⢿⣿⡿⠋⣿⡏⠉⠀⠀⠀⣹⡞⠁⠀⠀⠀⠀⠀⠀⢸⡀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣆⡴⡟⢸⢸⢰⡄⠀⠀⣹⢱⠀⠀⠀⢰⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⢧\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⠃⣿⠀⠃⢸⢸⠘⡇⠀⠀⣿⢸⠀⠀⠀⠃⠀⢧⡄⢀⡴⠃⠀⠀⠀⠀⠘\n⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⢿⡧⣿⠀⠀⡸⣾⠀⡇⠀⠀⣯⡏⠀⠀⠀⠀⠀⣸⡷⣫⣴⠀⠀⠀⢀⠂⢀\n⠘⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣇⠀⠀⣿⠀⠀⡇⣿⠰⠇⠀⣸⢻⠇⠀⠀⠀⠀⢰⠿⠞⣫⢞⡠⠀⢀⠂⠀⢸\n⠀⠘⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⣏⠻⣦⣤⣿⠀⠀⢧⡇⠀⠀⠀⢹⣾⠀⠀⠀⠀⢠⡏⣠⣼⣋⣉⣀⣴⣁⣀⣀⡎\n⠀⠀⠈⢿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣷⡌⠙⠺⢭⡿⠀⠀⠸⠆⠀⠀⠀⢸⣿⡀⠀⠀⠀⡟⢀⡧⣄⣠⣠⣤⣤⣤⣀⣈⡇\n⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠿⠃⠀⠈⠢⠐⢤⣧⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⠀⠀⣼⠁⡼⠉⠛⠒⠒⠒⠒⠶⠶⢿⠁\n⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⢀⣤⣛⡛⠛⢢⠀⠀⢠⠈⢪⣻⡇⠀⠀⠀⠀⠀⠀⠐⠃⠀⠀⢰⠏⢸⡧⠤⠤⠤⢤⣀⣀⡀⠀⡾⠀\n⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⣀⣀⠤⠴⠒⠚⣩⠽⣿⠖⠋⠉⠀⠀⣦⠈⣧⠀⠈⣳⣼⡿⠛⠀⠀⠀⠀⠀⠀⠀⢀⡤⠴⠞⠀⣿⠓⠢⠤⠤⠤⠤⣌⣉⣻⡇⠀\n⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣭⣶⣦⣤⣶⠋⢡⣴⠇⢀⣴⡦⠀⣠⢿⣤⣿⡴⠒⢹⣏⣀⠀⠀⢀⣀⣀⠀⠀⢀⣠⣄⢀⣤⣾⡯⡀⠀⠉⠒⠒⠤⢤⣭⣽⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⢠⣻⠃⡴⠛⢁⣴⡯⠇⠀⠀⠈⠉⠉⠉⢹⡍⠉⠉⠙⣷⠈⢻⠉⠻⠀⠘⣟⠻⠀⡉⠁⠀⠀⠀⠀⠀⠀⣠⣿⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣮⣵⢰⣧⣞⣶⡿⢋⣡⠔⠚⣀⡀⠀⠀⠀⠀⢨⠇⠀⠀⠀⢹⠀⠈⠁⠀⠀⠀⠿⠀⠀⠈⠓⠶⠄⠀⠐⣲⡾⠋⡿⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣾⡿⢿⣿⢎⢠⠟⡠⣾⠟⢋⡠⠤⠤⢤⠤⠾⠤⠤⣤⢤⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠞⠁⢀⣴⠇⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⡙⠻⣿⣿⣿⣿⣝⡋⣮⣴⣞⣥⡄⠀⠀⢀⣀⡤⠴⠚⠛⠪⣟⡧⢤⣄⣠⣄⡐⠦⣤⣤⣤⠴⠚⠉⠀⠀⠀⣾⠁⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⡄⠈⠙⢿⣿⣿⣿⣿⠟⠋⣁⣤⠴⠚⠉⠁⠀⠀⠀⠀⠀⠀⠉⠲⢤⡀⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⢀⣿⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⡄⠀⠀⢙⣹⣷⠶⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠦⣄⠀⠀⠀⠀⠀⠀⠀⠰⢚⡇⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⡾⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠂⠀⠀⠀⠀⠀⠈⠛⠃⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n      ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗ \n      ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║ \n      ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║ \n      ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║ \n      ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║ \n      ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝ \n\n'
                '\n'
                '\x1b[1;%dm%s%s\n'
                0.05
            [Disassembly]
                0       RESUME                          0
                2       LOAD_CONST                      1: '\x1b[0m'
                4       STORE_FAST                      0: clear
                6       BUILD_LIST                      0
                8       LOAD_CONST                      2: (35, 33, 36)
                10      LIST_EXTEND                     1
                12      STORE_FAST                      1: colors
                14      LOAD_CONST                      3: '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶⡎⠉⠀⠙⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠿⠉⠀⠀⠀⠀⠀⠈⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⣿⠛⠶⠤⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣥⣈⠉⠒⠦⣄⠀⣀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠛⠓⠲⣄⠈⠳⡌⠳⡀⠀⠀⠀⢸⣷⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⡇⠀⠀⠈⠳⡀⠈⢦⡹⡀⠀⠀⢸⠃⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠟⢳⣤⠀⢻⡿⣆⠀⢳⡗⠀⠀⡼⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣷⣤⡟⠀⠀⠈⠛⣆⠀⢷⠀⠀⡇⠀⠨⢧⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣧⣠⠀⠀⠀⠘⣆⠈⠃⣰⠁⠀⠄⠸⣦⡀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣷⡄⠀⠀⠀⠸⡅⢀⡏⠀⠀⠀⢠⠏⠱⣄⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣷⣤⣠⠖⢻⠁⡼⠀⠀⢀⡴⠋⠀⠀⠈⢦⡀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠉⢻⡻⣿⣿⣿⢧⣠⢏⣾⣡⠤⠚⣏⠀⠀⠀⠀⠀⠀⠉⠣⡄⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⡿⠁⢠⢿⣿⢿⣿⡿⠋⣿⡏⠉⠀⠀⠀⣹⡞⠁⠀⠀⠀⠀⠀⠀⢸⡀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣆⡴⡟⢸⢸⢰⡄⠀⠀⣹⢱⠀⠀⠀⢰⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⢧\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⠃⣿⠀⠃⢸⢸⠘⡇⠀⠀⣿⢸⠀⠀⠀⠃⠀⢧⡄⢀⡴⠃⠀⠀⠀⠀⠘\n⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⢿⡧⣿⠀⠀⡸⣾⠀⡇⠀⠀⣯⡏⠀⠀⠀⠀⠀⣸⡷⣫⣴⠀⠀⠀⢀⠂⢀\n⠘⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣇⠀⠀⣿⠀⠀⡇⣿⠰⠇⠀⣸⢻⠇⠀⠀⠀⠀⢰⠿⠞⣫⢞⡠⠀⢀⠂⠀⢸\n⠀⠘⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⣏⠻⣦⣤⣿⠀⠀⢧⡇⠀⠀⠀⢹⣾⠀⠀⠀⠀⢠⡏⣠⣼⣋⣉⣀⣴⣁⣀⣀⡎\n⠀⠀⠈⢿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣷⡌⠙⠺⢭⡿⠀⠀⠸⠆⠀⠀⠀⢸⣿⡀⠀⠀⠀⡟⢀⡧⣄⣠⣠⣤⣤⣤⣀⣈⡇\n⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠿⠃⠀⠈⠢⠐⢤⣧⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⠀⠀⣼⠁⡼⠉⠛⠒⠒⠒⠒⠶⠶⢿⠁\n⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⢀⣤⣛⡛⠛⢢⠀⠀⢠⠈⢪⣻⡇⠀⠀⠀⠀⠀⠀⠐⠃⠀⠀⢰⠏⢸⡧⠤⠤⠤⢤⣀⣀⡀⠀⡾⠀\n⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⣀⣀⠤⠴⠒⠚⣩⠽⣿⠖⠋⠉⠀⠀⣦⠈⣧⠀⠈⣳⣼⡿⠛⠀⠀⠀⠀⠀⠀⠀⢀⡤⠴⠞⠀⣿⠓⠢⠤⠤⠤⠤⣌⣉⣻⡇⠀\n⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣭⣶⣦⣤⣶⠋⢡⣴⠇⢀⣴⡦⠀⣠⢿⣤⣿⡴⠒⢹⣏⣀⠀⠀⢀⣀⣀⠀⠀⢀⣠⣄⢀⣤⣾⡯⡀⠀⠉⠒⠒⠤⢤⣭⣽⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⢠⣻⠃⡴⠛⢁⣴⡯⠇⠀⠀⠈⠉⠉⠉⢹⡍⠉⠉⠙⣷⠈⢻⠉⠻⠀⠘⣟⠻⠀⡉⠁⠀⠀⠀⠀⠀⠀⣠⣿⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣮⣵⢰⣧⣞⣶⡿⢋⣡⠔⠚⣀⡀⠀⠀⠀⠀⢨⠇⠀⠀⠀⢹⠀⠈⠁⠀⠀⠀⠿⠀⠀⠈⠓⠶⠄⠀⠐⣲⡾⠋⡿⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣾⡿⢿⣿⢎⢠⠟⡠⣾⠟⢋⡠⠤⠤⢤⠤⠾⠤⠤⣤⢤⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠞⠁⢀⣴⠇⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⡙⠻⣿⣿⣿⣿⣝⡋⣮⣴⣞⣥⡄⠀⠀⢀⣀⡤⠴⠚⠛⠪⣟⡧⢤⣄⣠⣄⡐⠦⣤⣤⣤⠴⠚⠉⠀⠀⠀⣾⠁⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⡄⠈⠙⢿⣿⣿⣿⣿⠟⠋⣁⣤⠴⠚⠉⠁⠀⠀⠀⠀⠀⠀⠉⠲⢤⡀⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⢀⣿⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⡄⠀⠀⢙⣹⣷⠶⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠦⣄⠀⠀⠀⠀⠀⠀⠀⠰⢚⡇⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⡾⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠂⠀⠀⠀⠀⠀⠈⠛⠃⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n      ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗ \n      ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║ \n      ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║ \n      ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║ \n      ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║ \n      ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝ \n\n'
                16      STORE_FAST                      2: x
                18      LOAD_GLOBAL                     1: NULL + enumerate
                30      LOAD_FAST                       2: x
                32      LOAD_METHOD                     1: split
                54      LOAD_CONST                      4: '\n'
                56      PRECALL                         1
                60      CALL                            1
                70      PRECALL                         1
                74      CALL                            1
                84      GET_ITER                        
                86      FOR_ITER                        80 (to 248)
                88      UNPACK_SEQUENCE                 2
                92      STORE_FAST                      3: N
                94      STORE_FAST                      4: line
                96      LOAD_GLOBAL                     4: sys
                108     LOAD_ATTR                       3: stdout
                118     LOAD_METHOD                     4: write
                140     LOAD_CONST                      5: '\x1b[1;%dm%s%s\n'
                142     LOAD_GLOBAL                     11: NULL + random
                154     LOAD_ATTR                       6: choice
                164     LOAD_FAST                       1: colors
                166     PRECALL                         1
                170     CALL                            1
                180     LOAD_FAST                       4: line
                182     LOAD_FAST                       0: clear
                184     BUILD_TUPLE                     3
                186     BINARY_OP                       6 (%)
                190     PRECALL                         1
                194     CALL                            1
                204     POP_TOP                         
                206     LOAD_GLOBAL                     15: NULL + time
                218     LOAD_ATTR                       8: sleep
                228     LOAD_CONST                      6: 0.05
                230     PRECALL                         1
                234     CALL                            1
                244     POP_TOP                         
                246     JUMP_BACKWARD                   81 (to 86)
                248     LOAD_CONST                      0: None
                250     RETURN_VALUE                    
        '\x1b[1;32m<<<<<<<<<<<<<<RAJPUT INXIDE<<<<<<<<<<<<<<<<<<<<<<<<\n'
        [Code]
            File Name: <x>
            Object Name: venom
            Qualified Name: venom
            Arg Count: 0
            Pos Only Arg Count: 0
            KW Only Arg Count: 0
            Stack Size: 2
            Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
            [Names]
            [Locals+Names]
                'clear'
                'colors'
            [Constants]
                None
                '\x1b[0m'
                (
                    35
                    33
                    36
                )
            [Disassembly]
                0       RESUME                          0
                2       LOAD_CONST                      1: '\x1b[0m'
                4       STORE_FAST                      0: clear
                6       BUILD_LIST                      0
                8       LOAD_CONST                      2: (35, 33, 36)
                10      LIST_EXTEND                     1
                12      STORE_FAST                      1: colors
                14      LOAD_CONST                      0: None
                16      RETURN_VALUE                    
        [Code]
            File Name: <x>
            Object Name: Subscraption
            Qualified Name: Subscraption
            Arg Count: 0
            Pos Only Arg Count: 0
            KW Only Arg Count: 0
            Stack Size: 6
            Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
            [Names]
                'os'
                'system'
                'time'
                'sleep'
                'str'
                'geteuid'
                'join'
                'print'
                'center'
                'get_terminal_size'
                'columns'
                'requests'
                'get'
                'text'
                'input'
                'Subscraption'
                'exit'
                'Exception'
                'sys'
            [Locals+Names]
                'uuid'
                'id'
                'logo'
                'httpCaht'
                'msg'
                'tks'
                'e'
            [Constants]
                None
                'git pull'
                1
                '#'
                'Premium-Tool-'
                ''
                'clear'
                "\n                                \n\n\x1b[38;5;46m /$$   /$$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$   /$$\n\x1b[1;36m| $$  | $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$| $$$ | $$\n\x1b[38;5;46m| $$  | $$| $$  \\ $$| $$  \\__/| $$  \\__/| $$  \\ $$| $$$$| $$\n\x1b[1;36m| $$$$$$$$| $$$$$$$$|  $$$$$$ |  $$$$$$ | $$$$$$$$| $$ $$ $$\n\x1b[38;5;46m| $$__  $$| $$__  $$ \\____  $$ \\____  $$| $$__  $$| $$  $$$$\n\x1b[1;36m| $$  | $$| $$  | $$ /$$  \\ $$ /$$  \\ $$| $$  | $$| $$\\  $$$\n\x1b[38;5;46m| $$  | $$| $$  | $$|  $$$$$$/|  $$$$$$/| $$  | $$| $$ \\  $$\n\x1b[1;36m|__/  |__/|__/  |__/ \\______/  \\______/ |__/  |__/|__/  \\__/\n                                                                                                                                                                                \n    \x1b[38;5;46m  /$$$$$$$   /$$$$$$     /$$$$$ /$$$$$$$  /$$   /$$ /$$$$$$$$\n   \x1b[38;5;46m  | $$__  $$ /$$__  $$   |__  $$| $$__  $$| $$  | $$|__  $$__/\n   \x1b[1;36m  | $$  \\ $$| $$  \\ $$      | $$| $$  \\ $$| $$  | $$   | $$   \n   \x1b[38;5;46m  | $$$$$$$/| $$$$$$$$      | $$| $$$$$$$/| $$  | $$   | $$   \n   \x1b[1;36m  | $$__  $$| $$__  $$ /$$  | $$| $$____/ | $$  | $$   | $$   \n   \x1b[38;5;46m  | $$  \\ $$| $$  | $$| $$  | $$| $$      | $$  | $$   | $$   \n     | $$  | $$| $$  | $$|  $$$$$$/| $$      |  $$$$$$/   | $$   \n  \x1b[1;36m   |__/  |__/|__/  |__/ \\______/ |__/       \\______/    |__/   \n                                                            \n                                                            \n\x1b[1;36m  ╔═════════════════【 𝐏𝐎𝐒𝐓 𝐌𝐔𝐋𝐓𝐘 𝐂𝐎𝐎𝐊𝐈𝐄 𝐓𝐎𝐎𝐋 】═════════════════╗\n\n\x1b[38;5;46m      ༶•┈┈⛧┈♛ 𝙾𝚆𝙽𝙴𝚁 𝚆𝙷𝙰𝚃'𝚂𝙰𝙿𝙿 𝙲𝙾𝙽𝚃𝙰𝙲𝚃 𝙽𝙾 +923417885339 ♛┈⛧┈┈•༶\n             \n\x1b[1;36m ╚═════════════════【 𝐇𝐑 𝐅𝐀𝐓𝐄𝐑 𝐎𝐅𝐅 𝐀𝐋𝐋 𝐑𝐔𝐋𝐄𝐗 】═════════════════╝\n\n\x1b[38;5;214m___________________________________________________________________\n\n\x1b[38;5;46m   ▄︻デ══━一【 𝐓𝐎𝐎𝐋 𝐎𝐖𝐍𝐄𝐑 𝐍𝐀𝐌𝐄 】 \x1b[1;36m➣ \x1b[38;5;46m【 𝐇𝐀𝐒𝐒𝐀𝐍 𝐑𝐀𝐉𝐏𝐔𝐓 】╾━╤デ╦︻▄\n\x1b[38;5;214m___________________________________________________________________\n\n\x1b[1;36m  ╔═════════════════════【 𝐖𝐀𝐋𝐋 𝐅𝐔𝐂𝐊𝐄𝐑 𝐓𝐎𝐎𝐋 】══════════════════╗\n\x1b[38;5;46m         【 𝐅𝐁 𝐏𝐀𝐆𝐄 + 𝐒𝐈𝐌𝐏𝐋𝐄 + 𝐂 𝐔𝐒𝐄𝐑 𝐈𝐃𝐙 𝐂𝐎𝐎𝐊𝐈𝐄 𝐓𝐎𝐎𝐋 】        \n\x1b[1;36m ╚════════════════════【 𝐇𝐀𝐒𝐒𝐀𝐍 𝐑𝐀𝐉𝐏𝐔𝐓 𝐇𝐄𝐑𝐄 】═════════════════╝\n                                "
                '\x1b[1;32;33m[•]\x1b[1;37m YOU NEED APROVAL TO USE THIS TOOL \x1b[1;37m'
                '\x1b[1;32;33m[•]\x1b[1;33m YOUR KEY :\x1b[1;37m '
                0.1
                '\x1b[33m--------------------------------------------------'
                'https://pastebin.com/raw/ceRZ6FXD'
                '\x1b[1;32;33m[•]\x1b[1;32m YOUR KEY HAS BEEN APROVED SUCESSFULLY'
                '\n\x1b[1;31m Your Key Not approved please contact the Owner'
                '\n\nPress Enter to send your key'
                "HASSAN%20RAJPUT,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Email%20:%20'+lol+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20"
                'am start https://wa.me/+923417885339?text='
                2
            [Disassembly]
                0       RESUME                          0
                2       LOAD_GLOBAL                     1: NULL + os
                14      LOAD_ATTR                       1: system
                24      LOAD_CONST                      1: 'git pull'
                26      PRECALL                         1
                30      CALL                            1
                40      POP_TOP                         
                42      LOAD_GLOBAL                     5: NULL + time
                54      LOAD_ATTR                       3: sleep
                64      LOAD_CONST                      2: 1
                66      PRECALL                         1
                70      CALL                            1
                80      POP_TOP                         
                82      LOAD_GLOBAL                     9: NULL + str
                94      LOAD_GLOBAL                     1: NULL + os
                106     LOAD_ATTR                       5: geteuid
                116     PRECALL                         0
                120     CALL                            0
                130     PRECALL                         1
                134     CALL                            1
                144     LOAD_CONST                      3: '#'
                146     BINARY_OP                       0 (+)
                150     LOAD_GLOBAL                     9: NULL + str
                162     LOAD_GLOBAL                     1: NULL + os
                174     LOAD_ATTR                       5: geteuid
                184     PRECALL                         0
                188     CALL                            0
                198     PRECALL                         1
                202     CALL                            1
                212     BINARY_OP                       0 (+)
                216     STORE_FAST                      0: uuid
                218     LOAD_CONST                      4: 'Premium-Tool-'
                220     LOAD_CONST                      5: ''
                222     LOAD_METHOD                     6: join
                244     LOAD_FAST                       0: uuid
                246     PRECALL                         1
                250     CALL                            1
                260     BINARY_OP                       0 (+)
                264     STORE_FAST                      1: id
                266     LOAD_GLOBAL                     1: NULL + os
                278     LOAD_ATTR                       1: system
                288     LOAD_CONST                      6: 'clear'
                290     PRECALL                         1
                294     CALL                            1
                304     POP_TOP                         
                306     LOAD_CONST                      7: "\n                                \n\n\x1b[38;5;46m /$$   /$$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$   /$$\n\x1b[1;36m| $$  | $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$| $$$ | $$\n\x1b[38;5;46m| $$  | $$| $$  \\ $$| $$  \\__/| $$  \\__/| $$  \\ $$| $$$$| $$\n\x1b[1;36m| $$$$$$$$| $$$$$$$$|  $$$$$$ |  $$$$$$ | $$$$$$$$| $$ $$ $$\n\x1b[38;5;46m| $$__  $$| $$__  $$ \\____  $$ \\____  $$| $$__  $$| $$  $$$$\n\x1b[1;36m| $$  | $$| $$  | $$ /$$  \\ $$ /$$  \\ $$| $$  | $$| $$\\  $$$\n\x1b[38;5;46m| $$  | $$| $$  | $$|  $$$$$$/|  $$$$$$/| $$  | $$| $$ \\  $$\n\x1b[1;36m|__/  |__/|__/  |__/ \\______/  \\______/ |__/  |__/|__/  \\__/\n                                                                                                                                                                                \n    \x1b[38;5;46m  /$$$$$$$   /$$$$$$     /$$$$$ /$$$$$$$  /$$   /$$ /$$$$$$$$\n   \x1b[38;5;46m  | $$__  $$ /$$__  $$   |__  $$| $$__  $$| $$  | $$|__  $$__/\n   \x1b[1;36m  | $$  \\ $$| $$  \\ $$      | $$| $$  \\ $$| $$  | $$   | $$   \n   \x1b[38;5;46m  | $$$$$$$/| $$$$$$$$      | $$| $$$$$$$/| $$  | $$   | $$   \n   \x1b[1;36m  | $$__  $$| $$__  $$ /$$  | $$| $$____/ | $$  | $$   | $$   \n   \x1b[38;5;46m  | $$  \\ $$| $$  | $$| $$  | $$| $$      | $$  | $$   | $$   \n     | $$  | $$| $$  | $$|  $$$$$$/| $$      |  $$$$$$/   | $$   \n  \x1b[1;36m   |__/  |__/|__/  |__/ \\______/ |__/       \\______/    |__/   \n                                                            \n                                                            \n\x1b[1;36m  ╔═════════════════【 𝐏𝐎𝐒𝐓 𝐌𝐔𝐋𝐓𝐘 𝐂𝐎𝐎𝐊𝐈𝐄 𝐓𝐎𝐎𝐋 】═════════════════╗\n\n\x1b[38;5;46m      ༶•┈┈⛧┈♛ 𝙾𝚆𝙽𝙴𝚁 𝚆𝙷𝙰𝚃'𝚂𝙰𝙿𝙿 𝙲𝙾𝙽𝚃𝙰𝙲𝚃 𝙽𝙾 +923417885339 ♛┈⛧┈┈•༶\n             \n\x1b[1;36m ╚═════════════════【 𝐇𝐑 𝐅𝐀𝐓𝐄𝐑 𝐎𝐅𝐅 𝐀𝐋𝐋 𝐑𝐔𝐋𝐄𝐗 】═════════════════╝\n\n\x1b[38;5;214m___________________________________________________________________\n\n\x1b[38;5;46m   ▄︻デ══━一【 𝐓𝐎𝐎𝐋 𝐎𝐖𝐍𝐄𝐑 𝐍𝐀𝐌𝐄 】 \x1b[1;36m➣ \x1b[38;5;46m【 𝐇𝐀𝐒𝐒𝐀𝐍 𝐑𝐀𝐉𝐏𝐔𝐓 】╾━╤デ╦︻▄\n\x1b[38;5;214m___________________________________________________________________\n\n\x1b[1;36m  ╔═════════════════════【 𝐖𝐀𝐋𝐋 𝐅𝐔𝐂𝐊𝐄𝐑 𝐓𝐎𝐎𝐋 】══════════════════╗\n\x1b[38;5;46m         【 𝐅𝐁 𝐏𝐀𝐆𝐄 + 𝐒𝐈𝐌𝐏𝐋𝐄 + 𝐂 𝐔𝐒𝐄𝐑 𝐈𝐃𝐙 𝐂𝐎𝐎𝐊𝐈𝐄 𝐓𝐎𝐎𝐋 】        \n\x1b[1;36m ╚════════════════════【 𝐇𝐀𝐒𝐒𝐀𝐍 𝐑𝐀𝐉𝐏𝐔𝐓 𝐇𝐄𝐑𝐄 】═════════════════╝\n                                "
                308     STORE_FAST                      2: logo
                310     LOAD_GLOBAL                     15: NULL + print
                322     LOAD_FAST                       2: logo
                324     LOAD_METHOD                     8: center
                346     LOAD_GLOBAL                     1: NULL + os
                358     LOAD_ATTR                       9: get_terminal_size
                368     PRECALL                         0
                372     CALL                            0
                382     LOAD_ATTR                       10: columns
                392     PRECALL                         1
                396     CALL                            1
                406     PRECALL                         1
                410     CALL                            1
                420     POP_TOP                         
                422     LOAD_GLOBAL                     15: NULL + print
                434     LOAD_CONST                      8: '\x1b[1;32;33m[•]\x1b[1;37m YOU NEED APROVAL TO USE THIS TOOL \x1b[1;37m'
                436     PRECALL                         1
                440     CALL                            1
                450     POP_TOP                         
                452     LOAD_GLOBAL                     15: NULL + print
                464     LOAD_CONST                      9: '\x1b[1;32;33m[•]\x1b[1;33m YOUR KEY :\x1b[1;37m '
                466     LOAD_FAST                       1: id
                468     BINARY_OP                       0 (+)
                472     PRECALL                         1
                476     CALL                            1
                486     POP_TOP                         
                488     LOAD_GLOBAL                     5: NULL + time
                500     LOAD_ATTR                       3: sleep
                510     LOAD_CONST                      10: 0.1
                512     PRECALL                         1
                516     CALL                            1
                526     POP_TOP                         
                528     LOAD_GLOBAL                     15: NULL + print
                540     LOAD_CONST                      11: '\x1b[33m--------------------------------------------------'
                542     PRECALL                         1
                546     CALL                            1
                556     POP_TOP                         
                558     NOP                             
                560     LOAD_GLOBAL                     23: NULL + requests
                572     LOAD_ATTR                       12: get
                582     LOAD_CONST                      12: 'https://pastebin.com/raw/ceRZ6FXD'
                584     PRECALL                         1
                588     CALL                            1
                598     LOAD_ATTR                       13: text
                608     STORE_FAST                      3: httpCaht
                610     LOAD_FAST                       1: id
                612     LOAD_FAST                       3: httpCaht
                614     CONTAINS_OP                     0 (in)
                616     POP_JUMP_FORWARD_IF_FALSE       69 (to 756)
                618     LOAD_GLOBAL                     15: NULL + print
                630     LOAD_CONST                      13: '\x1b[1;32;33m[•]\x1b[1;32m YOUR KEY HAS BEEN APROVED SUCESSFULLY'
                632     PRECALL                         1
                636     CALL                            1
                646     POP_TOP                         
                648     LOAD_GLOBAL                     9: NULL + str
                660     LOAD_GLOBAL                     1: NULL + os
                672     LOAD_ATTR                       5: geteuid
                682     PRECALL                         0
                686     CALL                            0
                696     PRECALL                         1
                700     CALL                            1
                710     STORE_FAST                      4: msg
                712     LOAD_GLOBAL                     5: NULL + time
                724     LOAD_ATTR                       3: sleep
                734     LOAD_CONST                      2: 1
                736     PRECALL                         1
                740     CALL                            1
                750     POP_TOP                         
                752     LOAD_CONST                      0: None
                754     RETURN_VALUE                    
                756     LOAD_GLOBAL                     15: NULL + print
                768     LOAD_CONST                      14: '\n\x1b[1;31m Your Key Not approved please contact the Owner'
                770     PRECALL                         1
                774     CALL                            1
                784     POP_TOP                         
                786     LOAD_GLOBAL                     5: NULL + time
                798     LOAD_ATTR                       3: sleep
                808     LOAD_CONST                      10: 0.1
                810     PRECALL                         1
                814     CALL                            1
                824     POP_TOP                         
                826     LOAD_GLOBAL                     29: NULL + input
                838     LOAD_CONST                      15: '\n\nPress Enter to send your key'
                840     PRECALL                         1
                844     CALL                            1
                854     POP_TOP                         
                856     LOAD_CONST                      16: "HASSAN%20RAJPUT,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Email%20:%20'+lol+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20"
                858     LOAD_FAST                       1: id
                860     BINARY_OP                       0 (+)
                864     STORE_FAST                      5: tks
                866     LOAD_GLOBAL                     1: NULL + os
                878     LOAD_ATTR                       1: system
                888     LOAD_CONST                      17: 'am start https://wa.me/+923417885339?text='
                890     LOAD_FAST                       5: tks
                892     BINARY_OP                       0 (+)
                896     PRECALL                         1
                900     CALL                            1
                910     LOAD_GLOBAL                     31: NULL + Subscraption
                922     PRECALL                         0
                926     CALL                            0
                936     BUILD_TUPLE                     2
                938     POP_TOP                         
                940     LOAD_GLOBAL                     5: NULL + time
                952     LOAD_ATTR                       3: sleep
                962     LOAD_CONST                      2: 1
                964     PRECALL                         1
                968     CALL                            1
                978     POP_TOP                         
                980     LOAD_GLOBAL                     33: NULL + exit
                992     PRECALL                         0
                996     CALL                            0
                1006    POP_TOP                         
                1008    LOAD_CONST                      0: None
                1010    RETURN_VALUE                    
                1012    PUSH_EXC_INFO                   
                1014    LOAD_GLOBAL                     34: Exception
                1026    CHECK_EXC_MATCH                 
                1028    POP_JUMP_FORWARD_IF_FALSE       60 (to 1150)
                1030    STORE_FAST                      6: e
                1032    LOAD_GLOBAL                     15: NULL + print
                1044    LOAD_FAST                       6: e
                1046    PRECALL                         1
                1050    CALL                            1
                1060    POP_TOP                         
                1062    LOAD_GLOBAL                     5: NULL + time
                1074    LOAD_ATTR                       3: sleep
                1084    LOAD_CONST                      18: 2
                1086    PRECALL                         1
                1090    CALL                            1
                1100    POP_TOP                         
                1102    LOAD_GLOBAL                     31: NULL + Subscraption
                1114    PRECALL                         0
                1118    CALL                            0
                1128    POP_TOP                         
                1130    POP_EXCEPT                      
                1132    LOAD_CONST                      0: None
                1134    STORE_FAST                      6: e
                1136    DELETE_FAST                     6: e
                1138    LOAD_CONST                      0: None
                1140    RETURN_VALUE                    
                1142    LOAD_CONST                      0: None
                1144    STORE_FAST                      6: e
                1146    DELETE_FAST                     6: e
                1148    RERAISE                         1
                1150    POP_TOP                         
                1152    LOAD_GLOBAL                     37: NULL + sys
                1164    LOAD_ATTR                       16: exit
                1174    PRECALL                         0
                1178    CALL                            0
                1188    POP_TOP                         
                1190    POP_EXCEPT                      
                1192    LOAD_CONST                      0: None
                1194    RETURN_VALUE                    
                1196    COPY                            3
                1198    POP_EXCEPT                      
                1200    RERAISE                         1
        [Code]
            File Name: <x>
            Object Name: pas
            Qualified Name: pas
            Arg Count: 0
            Pos Only Arg Count: 0
            KW Only Arg Count: 0
            Stack Size: 3
            Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
            [Names]
                'input'
                'requests'
                'get'
                'text'
                'print'
                'sys'
                'exit'
            [Locals+Names]
                'password'
                'mmm'
            [Constants]
                None
                '\x1b[1;32;33m[•] Enter Tool Passwrod  :: '
                'https://pastebin.com/raw/0CXjb7QN'
                '\x1b[1;32;31m[•] <==> Incorrect Password!'
            [Disassembly]
                0       RESUME                          0
                2       LOAD_GLOBAL                     1: NULL + input
                14      LOAD_CONST                      1: '\x1b[1;32;33m[•] Enter Tool Passwrod  :: '
                16      PRECALL                         1
                20      CALL                            1
                30      STORE_FAST                      0: password
                32      LOAD_GLOBAL                     3: NULL + requests
                44      LOAD_ATTR                       2: get
                54      LOAD_CONST                      2: 'https://pastebin.com/raw/0CXjb7QN'
                56      PRECALL                         1
                60      CALL                            1
                70      LOAD_ATTR                       3: text
                80      STORE_FAST                      1: mmm
                82      LOAD_FAST                       1: mmm
                84      LOAD_FAST                       0: password
                86      CONTAINS_OP                     1 (not in)
                88      POP_JUMP_FORWARD_IF_FALSE       36 (to 162)
                90      LOAD_GLOBAL                     9: NULL + print
                102     LOAD_CONST                      3: '\x1b[1;32;31m[•] <==> Incorrect Password!'
                104     PRECALL                         1
                108     CALL                            1
                118     POP_TOP                         
                120     LOAD_GLOBAL                     11: NULL + sys
                132     LOAD_ATTR                       6: exit
                142     PRECALL                         0
                146     CALL                            0
                156     POP_TOP                         
                158     LOAD_CONST                      0: None
                160     RETURN_VALUE                    
                162     LOAD_CONST                      0: None
                164     RETURN_VALUE                    
        '\x1b[1;32;33m[•] \x1b[1;36mTime start now:'
        '%Y-%m-%d %H:%M:%S'
        [Code]
            File Name: <x>
            Object Name: FacebookCommenter
            Qualified Name: FacebookCommenter
            Arg Count: 0
            Pos Only Arg Count: 0
            KW Only Arg Count: 0
            Stack Size: 1
            Flags: 0x00000000
            [Names]
                '__name__'
                '__module__'
                '__qualname__'
                '__init__'
                'comment_on_post'
                'inputs'
            [Locals+Names]
            [Constants]
                'FacebookCommenter'
                [Code]
                    File Name: <x>
                    Object Name: __init__
                    Qualified Name: FacebookCommenter.__init__
                    Arg Count: 1
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 2
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'comment_count'
                    [Locals+Names]
                        'self'
                    [Constants]
                        None
                        0
                    [Disassembly]
                        0       RESUME                          0
                        2       LOAD_CONST                      1: 0
                        4       LOAD_FAST                       0: self
                        6       STORE_ATTR                      0: comment_count
                        16      LOAD_CONST                      0: None
                        18      RETURN_VALUE                    
                [Code]
                    File Name: <x>
                    Object Name: comment_on_post
                    Qualified Name: FacebookCommenter.comment_on_post
                    Arg Count: 5
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 14
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'requests'
                        'Session'
                        'headers'
                        'update'
                        'get'
                        'format'
                        're'
                        'search'
                        'text'
                        'group'
                        'replace'
                        'next_action'
                        'print'
                        'fb_dtsg'
                        'jazoest'
                        'post'
                        'str'
                        'url'
                        'status_code'
                        'comment_count'
                        'sys'
                        'stdout'
                        'write'
                        'flush'
                        'datetime'
                        'now'
                        'strftime'
                    [Locals+Names]
                        'self'
                        'cookies'
                        'post_id'
                        'comment'
                        'timm'
                        'r'
                        'response'
                        'next_action_match'
                        'fb_dtsg_match'
                        'jazoest_match'
                        'data'
                        'response2'
                        'e'
                    [Constants]
                        None
                        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7'
                        'none'
                        'id,en;q=0.9'
                        'mbasic.facebook.com'
                        '?1'
                        'document'
                        'gzip, deflate'
                        'navigate'
                        'Mozilla/5.0 (Linux; Android 13; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36'
                        'keep-alive'
                        (
                            'accept'
                            'sec-fetch-site'
                            'accept-language'
                            'Host'
                            'sec-fetch-user'
                            'sec-fetch-dest'
                            'accept-encoding'
                            'sec-fetch-mode'
                            'user-agent'
                            'connection'
                        )
                        'https://mbasic.facebook.com/{}'
                        'cookie'
                        (
                            'cookies'
                        )
                        'method="post" action="([^"]+)"'
                        1
                        'amp;'
                        ''
                        '\x1b[1;37;1m  Coockies Chack =>C_USER ID<= i_USER \x1b[1;32;31m'
                        '\x1b[1;34mThe Comment is ready to go on the post'
                        'name="fb_dtsg" value="([^"]+)"'
                        '\x1b[1;35;1m Your Cookie File Complete Restart your Cookie file\x1b[1;32;31m'
                        'name="jazoest" value="([^"]+)"'
                        '<Error> jazoest not found'
                        'Submit'
                        (
                            'fb_dtsg'
                            'jazoest'
                            'comment_text'
                            'comment'
                        )
                        'application/x-www-form-urlencoded'
                        'https://mbasic.facebook.com'
                        (
                            'content-type'
                            'referer'
                            'origin'
                        )
                        'https://mbasic.facebook.com{}'
                        (
                            'data'
                            'cookies'
                        )
                        'comment_success'
                        200
                        '\rComment count: '
                        'Comment successfully posted: '
                        '\n\x1b[1;92m   \x1b[1;37m[ <============>『 𝐇𝐀𝐒𝐒𝐀𝐍 𝐑𝐀𝐉𝐏𝐔𝐓 𝐌𝐔𝐋𝐓𝐘 𝐖𝐀𝐋𝐋 』<============> ]'
                        '\x1b[1;32;40m YOUR ID STATUS :: ACTIVE'
                        '\x1b[1;33m DATE :: %d-%m-%Y '
                        '\x1b[1;33m TIME :: %I:%M:%S %p'
                        '\x1b[1;32;40m COMMENT SEND SUCESSFULLY ⚜️  :: '
                    [Disassembly]
                        0       RESUME                          0
                        2       LOAD_GLOBAL                     1: NULL + requests
                        14      LOAD_ATTR                       1: Session
                        24      PRECALL                         0
                        28      CALL                            0
                        38      BEFORE_WITH                     
                        40      STORE_FAST                      5: r
                        42      LOAD_FAST                       5: r
                        44      LOAD_ATTR                       2: headers
                        54      LOAD_METHOD                     3: update
                        76      LOAD_CONST                      1: 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7'
                        78      LOAD_CONST                      2: 'none'
                        80      LOAD_CONST                      3: 'id,en;q=0.9'
                        82      LOAD_CONST                      4: 'mbasic.facebook.com'
                        84      LOAD_CONST                      5: '?1'
                        86      LOAD_CONST                      6: 'document'
                        88      LOAD_CONST                      7: 'gzip, deflate'
                        90      LOAD_CONST                      8: 'navigate'
                        92      LOAD_CONST                      9: 'Mozilla/5.0 (Linux; Android 13; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36'
                        94      LOAD_CONST                      10: 'keep-alive'
                        96      LOAD_CONST                      11: ('accept', 'sec-fetch-site', 'accept-language', 'Host', 'sec-fetch-user', 'sec-fetch-dest', 'accept-encoding', 'sec-fetch-mode', 'user-agent', 'connection')
                        98      BUILD_CONST_KEY_MAP             10
                        100     PRECALL                         1
                        104     CALL                            1
                        114     POP_TOP                         
                        116     LOAD_FAST                       5: r
                        118     LOAD_METHOD                     4: get
                        140     LOAD_CONST                      12: 'https://mbasic.facebook.com/{}'
                        142     LOAD_METHOD                     5: format
                        164     LOAD_FAST                       2: post_id
                        166     PRECALL                         1
                        170     CALL                            1
                        180     LOAD_CONST                      13: 'cookie'
                        182     LOAD_FAST                       1: cookies
                        184     BUILD_MAP                       1
                        186     KW_NAMES                        14: ('cookies',)
                        188     PRECALL                         2
                        192     CALL                            2
                        202     STORE_FAST                      6: response
                        204     LOAD_GLOBAL                     13: NULL + re
                        216     LOAD_ATTR                       7: search
                        226     LOAD_CONST                      15: 'method="post" action="([^"]+)"'
                        228     LOAD_FAST                       6: response
                        230     LOAD_ATTR                       8: text
                        240     PRECALL                         2
                        244     CALL                            2
                        254     STORE_FAST                      7: next_action_match
                        256     LOAD_FAST                       7: next_action_match
                        258     POP_JUMP_FORWARD_IF_FALSE       47 (to 354)
                        260     LOAD_FAST                       7: next_action_match
                        262     LOAD_METHOD                     9: group
                        284     LOAD_CONST                      16: 1
                        286     PRECALL                         1
                        290     CALL                            1
                        300     LOAD_METHOD                     10: replace
                        322     LOAD_CONST                      17: 'amp;'
                        324     LOAD_CONST                      18: ''
                        326     PRECALL                         2
                        330     CALL                            2
                        340     LOAD_FAST                       0: self
                        342     STORE_ATTR                      11: next_action
                        352     JUMP_FORWARD                    34 (to 422)
                        354     LOAD_GLOBAL                     25: NULL + print
                        366     LOAD_CONST                      19: '\x1b[1;37;1m  Coockies Chack =>C_USER ID<= i_USER \x1b[1;32;31m'
                        368     LOAD_FAST                       0: self
                        370     LOAD_FAST                       1: cookies
                        372     BUILD_TUPLE                     2
                        374     FORMAT_VALUE                    0
                        376     BUILD_STRING                    2
                        378     PRECALL                         1
                        382     CALL                            1
                        392     POP_TOP                         
                        394     NOP                             
                        396     LOAD_CONST                      0: None
                        398     LOAD_CONST                      0: None
                        400     LOAD_CONST                      0: None
                        402     PRECALL                         2
                        406     CALL                            2
                        416     POP_TOP                         
                        418     LOAD_CONST                      0: None
                        420     RETURN_VALUE                    
                        422     LOAD_GLOBAL                     13: NULL + re
                        434     LOAD_ATTR                       7: search
                        444     LOAD_CONST                      21: 'name="fb_dtsg" value="([^"]+)"'
                        446     LOAD_FAST                       6: response
                        448     LOAD_ATTR                       8: text
                        458     PRECALL                         2
                        462     CALL                            2
                        472     STORE_FAST                      8: fb_dtsg_match
                        474     LOAD_FAST                       8: fb_dtsg_match
                        476     POP_JUMP_FORWARD_IF_FALSE       27 (to 532)
                        478     LOAD_FAST                       8: fb_dtsg_match
                        480     LOAD_METHOD                     9: group
                        502     LOAD_CONST                      16: 1
                        504     PRECALL                         1
                        508     CALL                            1
                        518     LOAD_FAST                       0: self
                        520     STORE_ATTR                      13: fb_dtsg
                        530     JUMP_FORWARD                    34 (to 600)
                        532     LOAD_GLOBAL                     25: NULL + print
                        544     LOAD_CONST                      22: '\x1b[1;35;1m Your Cookie File Complete Restart your Cookie file\x1b[1;32;31m'
                        546     LOAD_FAST                       0: self
                        548     LOAD_FAST                       1: cookies
                        550     BUILD_TUPLE                     2
                        552     FORMAT_VALUE                    0
                        554     BUILD_STRING                    2
                        556     PRECALL                         1
                        560     CALL                            1
                        570     POP_TOP                         
                        572     NOP                             
                        574     LOAD_CONST                      0: None
                        576     LOAD_CONST                      0: None
                        578     LOAD_CONST                      0: None
                        580     PRECALL                         2
                        584     CALL                            2
                        594     POP_TOP                         
                        596     LOAD_CONST                      0: None
                        598     RETURN_VALUE                    
                        600     LOAD_GLOBAL                     13: NULL + re
                        612     LOAD_ATTR                       7: search
                        622     LOAD_CONST                      23: 'name="jazoest" value="([^"]+)"'
                        624     LOAD_FAST                       6: response
                        626     LOAD_ATTR                       8: text
                        636     PRECALL                         2
                        640     CALL                            2
                        650     STORE_FAST                      9: jazoest_match
                        652     LOAD_FAST                       9: jazoest_match
                        654     POP_JUMP_FORWARD_IF_FALSE       27 (to 710)
                        656     LOAD_FAST                       9: jazoest_match
                        658     LOAD_METHOD                     9: group
                        680     LOAD_CONST                      16: 1
                        682     PRECALL                         1
                        686     CALL                            1
                        696     LOAD_FAST                       0: self
                        698     STORE_ATTR                      14: jazoest
                        708     JUMP_FORWARD                    29 (to 768)
                        710     LOAD_GLOBAL                     25: NULL + print
                        722     LOAD_CONST                      24: '<Error> jazoest not found'
                        724     PRECALL                         1
                        728     CALL                            1
                        738     POP_TOP                         
                        740     NOP                             
                        742     LOAD_CONST                      0: None
                        744     LOAD_CONST                      0: None
                        746     LOAD_CONST                      0: None
                        748     PRECALL                         2
                        752     CALL                            2
                        762     POP_TOP                         
                        764     LOAD_CONST                      0: None
                        766     RETURN_VALUE                    
                        768     LOAD_FAST                       0: self
                        770     LOAD_ATTR                       13: fb_dtsg
                        780     LOAD_FAST                       0: self
                        782     LOAD_ATTR                       14: jazoest
                        792     LOAD_FAST                       3: comment
                        794     LOAD_CONST                      25: 'Submit'
                        796     LOAD_CONST                      26: ('fb_dtsg', 'jazoest', 'comment_text', 'comment')
                        798     BUILD_CONST_KEY_MAP             4
                        800     STORE_FAST                      10: data
                        802     LOAD_FAST                       5: r
                        804     LOAD_ATTR                       2: headers
                        814     LOAD_METHOD                     3: update
                        836     LOAD_CONST                      27: 'application/x-www-form-urlencoded'
                        838     LOAD_CONST                      12: 'https://mbasic.facebook.com/{}'
                        840     LOAD_METHOD                     5: format
                        862     LOAD_FAST                       2: post_id
                        864     PRECALL                         1
                        868     CALL                            1
                        878     LOAD_CONST                      28: 'https://mbasic.facebook.com'
                        880     LOAD_CONST                      29: ('content-type', 'referer', 'origin')
                        882     BUILD_CONST_KEY_MAP             3
                        884     PRECALL                         1
                        888     CALL                            1
                        898     POP_TOP                         
                        900     LOAD_FAST                       5: r
                        902     LOAD_METHOD                     15: post
                        924     LOAD_CONST                      30: 'https://mbasic.facebook.com{}'
                        926     LOAD_METHOD                     5: format
                        948     LOAD_FAST                       0: self
                        950     LOAD_ATTR                       11: next_action
                        960     PRECALL                         1
                        964     CALL                            1
                        974     LOAD_FAST                       10: data
                        976     LOAD_CONST                      13: 'cookie'
                        978     LOAD_FAST                       1: cookies
                        980     BUILD_MAP                       1
                        982     KW_NAMES                        31: ('data', 'cookies')
                        984     PRECALL                         3
                        988     CALL                            3
                        998     STORE_FAST                      11: response2
                        1000    LOAD_CONST                      32: 'comment_success'
                        1002    LOAD_GLOBAL                     33: NULL + str
                        1014    LOAD_FAST                       11: response2
                        1016    LOAD_ATTR                       17: url
                        1026    PRECALL                         1
                        1030    CALL                            1
                        1040    CONTAINS_OP                     0 (in)
                        1042    POP_JUMP_FORWARD_IF_FALSE       115 (to 1274)
                        1044    LOAD_FAST                       11: response2
                        1046    LOAD_ATTR                       18: status_code
                        1056    LOAD_CONST                      33: 200
                        1058    COMPARE_OP                      2 (==)
                        1064    POP_JUMP_FORWARD_IF_FALSE       104 (to 1274)
                        1066    LOAD_FAST                       0: self
                        1068    COPY                            1
                        1070    LOAD_ATTR                       19: comment_count
                        1080    LOAD_CONST                      16: 1
                        1082    BINARY_OP                       13 (+=)
                        1086    SWAP                            2
                        1088    STORE_ATTR                      19: comment_count
                        1098    LOAD_GLOBAL                     40: sys
                        1110    LOAD_ATTR                       21: stdout
                        1120    LOAD_METHOD                     22: write
                        1142    LOAD_CONST                      34: '\rComment count: '
                        1144    LOAD_FAST                       0: self
                        1146    LOAD_ATTR                       19: comment_count
                        1156    FORMAT_VALUE                    0
                        1158    BUILD_STRING                    2
                        1160    PRECALL                         1
                        1164    CALL                            1
                        1174    POP_TOP                         
                        1176    LOAD_GLOBAL                     40: sys
                        1188    LOAD_ATTR                       21: stdout
                        1198    LOAD_METHOD                     23: flush
                        1220    PRECALL                         0
                        1224    CALL                            0
                        1234    POP_TOP                         
                        1236    LOAD_GLOBAL                     25: NULL + print
                        1248    LOAD_CONST                      35: 'Comment successfully posted: '
                        1250    LOAD_FAST                       3: comment
                        1252    FORMAT_VALUE                    0
                        1254    BUILD_STRING                    2
                        1256    PRECALL                         1
                        1260    CALL                            1
                        1270    POP_TOP                         
                        1272    JUMP_FORWARD                    135 (to 1544)
                        1274    LOAD_GLOBAL                     25: NULL + print
                        1286    LOAD_CONST                      36: '\n\x1b[1;92m   \x1b[1;37m[ <============>『 𝐇𝐀𝐒𝐒𝐀𝐍 𝐑𝐀𝐉𝐏𝐔𝐓 𝐌𝐔𝐋𝐓𝐘 𝐖𝐀𝐋𝐋 』<============> ]'
                        1288    PRECALL                         1
                        1292    CALL                            1
                        1302    POP_TOP                         
                        1304    LOAD_GLOBAL                     25: NULL + print
                        1316    LOAD_CONST                      37: '\x1b[1;32;40m YOUR ID STATUS :: ACTIVE'
                        1318    PRECALL                         1
                        1322    CALL                            1
                        1332    POP_TOP                         
                        1334    LOAD_GLOBAL                     49: NULL + datetime
                        1346    LOAD_ATTR                       25: now
                        1356    PRECALL                         0
                        1360    CALL                            0
                        1370    STORE_FAST                      12: e
                        1372    LOAD_GLOBAL                     25: NULL + print
                        1384    LOAD_FAST                       12: e
                        1386    LOAD_METHOD                     26: strftime
                        1408    LOAD_CONST                      38: '\x1b[1;33m DATE :: %d-%m-%Y '
                        1410    PRECALL                         1
                        1414    CALL                            1
                        1424    PRECALL                         1
                        1428    CALL                            1
                        1438    POP_TOP                         
                        1440    LOAD_GLOBAL                     25: NULL + print
                        1452    LOAD_FAST                       12: e
                        1454    LOAD_METHOD                     26: strftime
                        1476    LOAD_CONST                      39: '\x1b[1;33m TIME :: %I:%M:%S %p'
                        1478    PRECALL                         1
                        1482    CALL                            1
                        1492    PRECALL                         1
                        1496    CALL                            1
                        1506    POP_TOP                         
                        1508    LOAD_GLOBAL                     25: NULL + print
                        1520    LOAD_CONST                      40: '\x1b[1;32;40m COMMENT SEND SUCESSFULLY ⚜️  :: '
                        1522    LOAD_FAST                       3: comment
                        1524    FORMAT_VALUE                    0
                        1526    BUILD_STRING                    2
                        1528    PRECALL                         1
                        1532    CALL                            1
                        1542    POP_TOP                         
                        1544    LOAD_CONST                      0: None
                        1546    LOAD_CONST                      0: None
                        1548    LOAD_CONST                      0: None
                        1550    PRECALL                         2
                        1554    CALL                            2
                        1564    POP_TOP                         
                        1566    LOAD_CONST                      0: None
                        1568    RETURN_VALUE                    
                        1570    PUSH_EXC_INFO                   
                        1572    WITH_EXCEPT_START               
                        1574    POP_JUMP_FORWARD_IF_TRUE        4 (to 1584)
                        1576    RERAISE                         2
                        1578    COPY                            3
                        1580    POP_EXCEPT                      
                        1582    RERAISE                         1
                        1584    POP_TOP                         
                        1586    POP_EXCEPT                      
                        1588    POP_TOP                         
                        1590    POP_TOP                         
                        1592    LOAD_CONST                      0: None
                        1594    RETURN_VALUE                    
                [Code]
                    File Name: <x>
                    Object Name: inputs
                    Qualified Name: FacebookCommenter.inputs
                    Arg Count: 1
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 7
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'input'
                        'strip'
                        'open'
                        'read'
                        'splitlines'
                        'readlines'
                        'int'
                        'time'
                        'sleep'
                        'comment_on_post'
                        'len'
                        'RequestException'
                        'print'
                        'str'
                        'lower'
                        'Exception'
                        'KeyboardInterrupt'
                        'exit'
                    [Locals+Names]
                        'self'
                        'coockies_file_path'
                        'file'
                        'your_cookies'
                        'post_id'
                        'comments_file'
                        'comments'
                        'timm'
                        'cookie_index'
                        'comment'
                        'e'
                    [Constants]
                        None
                        '\x1b[1;32;33m[•]\x1b[38;5;46m Enter Cookie file Path  ::\x1b[1;34m '
                        'r'
                        '\x1b[1;32;33m[•]\x1b[1;33m Enter Your Post Uid  ::\x1b[1;35m '
                        '\x1b[1;32;33m[•]\x1b[1;36m Enter Comment file Path  ::\x1b[33m '
                        '\x1b[1;32;33m[•]\x1b[1;31m Enter time (speed in second  ::\x1b[1;32m '
                        0
                        True
                        1
                        '<chack first & last coockies> '
                    [Disassembly]
                        0       RESUME                          0
                        2       NOP                             
                        4       LOAD_GLOBAL                     1: NULL + input
                        16      LOAD_CONST                      1: '\x1b[1;32;33m[•]\x1b[38;5;46m Enter Cookie file Path  ::\x1b[1;34m '
                        18      PRECALL                         1
                        22      CALL                            1
                        32      LOAD_METHOD                     1: strip
                        54      PRECALL                         0
                        58      CALL                            0
                        68      STORE_FAST                      1: coockies_file_path
                        70      LOAD_GLOBAL                     5: NULL + open
                        82      LOAD_FAST                       1: coockies_file_path
                        84      LOAD_CONST                      2: 'r'
                        86      PRECALL                         2
                        90      CALL                            2
                        100     BEFORE_WITH                     
                        102     STORE_FAST                      2: file
                        104     LOAD_FAST                       2: file
                        106     LOAD_METHOD                     3: read
                        128     PRECALL                         0
                        132     CALL                            0
                        142     LOAD_METHOD                     4: splitlines
                        164     PRECALL                         0
                        168     CALL                            0
                        178     STORE_FAST                      3: your_cookies
                        180     LOAD_GLOBAL                     1: NULL + input
                        192     LOAD_CONST                      3: '\x1b[1;32;33m[•]\x1b[1;33m Enter Your Post Uid  ::\x1b[1;35m '
                        194     PRECALL                         1
                        198     CALL                            1
                        208     LOAD_METHOD                     1: strip
                        230     PRECALL                         0
                        234     CALL                            0
                        244     STORE_FAST                      4: post_id
                        246     LOAD_CONST                      0: None
                        248     LOAD_CONST                      0: None
                        250     LOAD_CONST                      0: None
                        252     PRECALL                         2
                        256     CALL                            2
                        266     POP_TOP                         
                        268     JUMP_FORWARD                    11 (to 292)
                        270     PUSH_EXC_INFO                   
                        272     WITH_EXCEPT_START               
                        274     POP_JUMP_FORWARD_IF_TRUE        4 (to 284)
                        276     RERAISE                         2
                        278     COPY                            3
                        280     POP_EXCEPT                      
                        282     RERAISE                         1
                        284     POP_TOP                         
                        286     POP_EXCEPT                      
                        288     POP_TOP                         
                        290     POP_TOP                         
                        292     LOAD_GLOBAL                     1: NULL + input
                        304     LOAD_CONST                      4: '\x1b[1;32;33m[•]\x1b[1;36m Enter Comment file Path  ::\x1b[33m '
                        306     PRECALL                         1
                        310     CALL                            1
                        320     LOAD_METHOD                     1: strip
                        342     PRECALL                         0
                        346     CALL                            0
                        356     STORE_FAST                      5: comments_file
                        358     LOAD_GLOBAL                     5: NULL + open
                        370     LOAD_FAST                       5: comments_file
                        372     LOAD_CONST                      2: 'r'
                        374     PRECALL                         2
                        378     CALL                            2
                        388     BEFORE_WITH                     
                        390     STORE_FAST                      2: file
                        392     LOAD_FAST                       2: file
                        394     LOAD_METHOD                     5: readlines
                        416     PRECALL                         0
                        420     CALL                            0
                        430     STORE_FAST                      6: comments
                        432     LOAD_CONST                      0: None
                        434     LOAD_CONST                      0: None
                        436     LOAD_CONST                      0: None
                        438     PRECALL                         2
                        442     CALL                            2
                        452     POP_TOP                         
                        454     JUMP_FORWARD                    11 (to 478)
                        456     PUSH_EXC_INFO                   
                        458     WITH_EXCEPT_START               
                        460     POP_JUMP_FORWARD_IF_TRUE        4 (to 470)
                        462     RERAISE                         2
                        464     COPY                            3
                        466     POP_EXCEPT                      
                        468     RERAISE                         1
                        470     POP_TOP                         
                        472     POP_EXCEPT                      
                        474     POP_TOP                         
                        476     POP_TOP                         
                        478     LOAD_GLOBAL                     13: NULL + int
                        490     LOAD_GLOBAL                     1: NULL + input
                        502     LOAD_CONST                      5: '\x1b[1;32;33m[•]\x1b[1;31m Enter time (speed in second  ::\x1b[1;32m '
                        504     PRECALL                         1
                        508     CALL                            1
                        518     LOAD_METHOD                     1: strip
                        540     PRECALL                         0
                        544     CALL                            0
                        554     PRECALL                         1
                        558     CALL                            1
                        568     STORE_FAST                      7: timm
                        570     LOAD_CONST                      6: 0
                        572     STORE_FAST                      8: cookie_index
                        574     NOP                             
                        576     NOP                             
                        578     LOAD_FAST                       6: comments
                        580     GET_ITER                        
                        582     FOR_ITER                        95 (to 774)
                        584     STORE_FAST                      9: comment
                        586     LOAD_FAST                       9: comment
                        588     LOAD_METHOD                     1: strip
                        610     PRECALL                         0
                        614     CALL                            0
                        624     STORE_FAST                      9: comment
                        626     LOAD_FAST                       9: comment
                        628     POP_JUMP_FORWARD_IF_FALSE       71 (to 772)
                        630     LOAD_GLOBAL                     15: NULL + time
                        642     LOAD_ATTR                       8: sleep
                        652     LOAD_FAST                       7: timm
                        654     PRECALL                         1
                        658     CALL                            1
                        668     POP_TOP                         
                        670     LOAD_FAST                       0: self
                        672     LOAD_METHOD                     9: comment_on_post
                        694     LOAD_FAST                       3: your_cookies
                        696     LOAD_FAST                       8: cookie_index
                        698     BINARY_SUBSCR                   
                        708     LOAD_FAST                       4: post_id
                        710     LOAD_FAST                       9: comment
                        712     LOAD_FAST                       7: timm
                        714     PRECALL                         4
                        718     CALL                            4
                        728     POP_TOP                         
                        730     LOAD_FAST                       8: cookie_index
                        732     LOAD_CONST                      8: 1
                        734     BINARY_OP                       0 (+)
                        738     LOAD_GLOBAL                     21: NULL + len
                        750     LOAD_FAST                       3: your_cookies
                        752     PRECALL                         1
                        756     CALL                            1
                        766     BINARY_OP                       6 (%)
                        770     STORE_FAST                      8: cookie_index
                        772     JUMP_BACKWARD                   96 (to 582)
                        774     JUMP_FORWARD                    151 (to 1078)
                        776     PUSH_EXC_INFO                   
                        778     LOAD_GLOBAL                     22: RequestException
                        790     CHECK_EXC_MATCH                 
                        792     POP_JUMP_FORWARD_IF_FALSE       59 (to 912)
                        794     STORE_FAST                      10: e
                        796     LOAD_GLOBAL                     25: NULL + print
                        808     LOAD_CONST                      9: '<chack first & last coockies> '
                        810     LOAD_GLOBAL                     27: NULL + str
                        822     LOAD_FAST                       10: e
                        824     PRECALL                         1
                        828     CALL                            1
                        838     LOAD_METHOD                     14: lower
                        860     PRECALL                         0
                        864     CALL                            0
                        874     FORMAT_VALUE                    0
                        876     BUILD_STRING                    2
                        878     PRECALL                         1
                        882     CALL                            1
                        892     POP_TOP                         
                        894     POP_EXCEPT                      
                        896     LOAD_CONST                      0: None
                        898     STORE_FAST                      10: e
                        900     DELETE_FAST                     10: e
                        902     JUMP_FORWARD                    87 (to 1078)
                        904     LOAD_CONST                      0: None
                        906     STORE_FAST                      10: e
                        908     DELETE_FAST                     10: e
                        910     RERAISE                         1
                        912     LOAD_GLOBAL                     30: Exception
                        924     CHECK_EXC_MATCH                 
                        926     POP_JUMP_FORWARD_IF_FALSE       59 (to 1046)
                        928     STORE_FAST                      10: e
                        930     LOAD_GLOBAL                     25: NULL + print
                        942     LOAD_CONST                      9: '<chack first & last coockies> '
                        944     LOAD_GLOBAL                     27: NULL + str
                        956     LOAD_FAST                       10: e
                        958     PRECALL                         1
                        962     CALL                            1
                        972     LOAD_METHOD                     14: lower
                        994     PRECALL                         0
                        998     CALL                            0
                        1008    FORMAT_VALUE                    0
                        1010    BUILD_STRING                    2
                        1012    PRECALL                         1
                        1016    CALL                            1
                        1026    POP_TOP                         
                        1028    POP_EXCEPT                      
                        1030    LOAD_CONST                      0: None
                        1032    STORE_FAST                      10: e
                        1034    DELETE_FAST                     10: e
                        1036    JUMP_FORWARD                    20 (to 1078)
                        1038    LOAD_CONST                      0: None
                        1040    STORE_FAST                      10: e
                        1042    DELETE_FAST                     10: e
                        1044    RERAISE                         1
                        1046    LOAD_GLOBAL                     32: KeyboardInterrupt
                        1058    CHECK_EXC_MATCH                 
                        1060    POP_JUMP_FORWARD_IF_FALSE       4 (to 1070)
                        1062    POP_TOP                         
                        1064    POP_EXCEPT                      
                        1066    LOAD_CONST                      0: None
                        1068    RETURN_VALUE                    
                        1070    RERAISE                         0
                        1072    COPY                            3
                        1074    POP_EXCEPT                      
                        1076    RERAISE                         1
                        1078    JUMP_BACKWARD                   252 (to 576)
                        1080    PUSH_EXC_INFO                   
                        1082    LOAD_GLOBAL                     30: Exception
                        1094    CHECK_EXC_MATCH                 
                        1096    POP_JUMP_FORWARD_IF_FALSE       74 (to 1246)
                        1098    STORE_FAST                      10: e
                        1100    LOAD_GLOBAL                     25: NULL + print
                        1112    LOAD_CONST                      9: '<chack first & last coockies> '
                        1114    LOAD_GLOBAL                     27: NULL + str
                        1126    LOAD_FAST                       10: e
                        1128    PRECALL                         1
                        1132    CALL                            1
                        1142    LOAD_METHOD                     14: lower
                        1164    PRECALL                         0
                        1168    CALL                            0
                        1178    FORMAT_VALUE                    0
                        1180    BUILD_STRING                    2
                        1182    PRECALL                         1
                        1186    CALL                            1
                        1196    POP_TOP                         
                        1198    LOAD_GLOBAL                     35: NULL + exit
                        1210    PRECALL                         0
                        1214    CALL                            0
                        1224    POP_TOP                         
                        1226    POP_EXCEPT                      
                        1228    LOAD_CONST                      0: None
                        1230    STORE_FAST                      10: e
                        1232    DELETE_FAST                     10: e
                        1234    LOAD_CONST                      0: None
                        1236    RETURN_VALUE                    
                        1238    LOAD_CONST                      0: None
                        1240    STORE_FAST                      10: e
                        1242    DELETE_FAST                     10: e
                        1244    RERAISE                         1
                        1246    RERAISE                         0
                        1248    COPY                            3
                        1250    POP_EXCEPT                      
                        1252    RERAISE                         1
                None
            [Disassembly]
                0       RESUME                          0
                2       LOAD_NAME                       0: __name__
                4       STORE_NAME                      1: __module__
                6       LOAD_CONST                      0: 'FacebookCommenter'
                8       STORE_NAME                      2: __qualname__
                10      LOAD_CONST                      1: <CODE> __init__
                12      MAKE_FUNCTION                   0
                14      STORE_NAME                      3: __init__
                16      LOAD_CONST                      2: <CODE> comment_on_post
                18      MAKE_FUNCTION                   0
                20      STORE_NAME                      4: comment_on_post
                22      LOAD_CONST                      3: <CODE> inputs
                24      MAKE_FUNCTION                   0
                26      STORE_NAME                      5: inputs
                28      LOAD_CONST                      4: None
                30      RETURN_VALUE                    
        'FacebookCommenter'
        '__main__'
    [Disassembly]
        0       RESUME                          0
        2       LOAD_CONST                      0: 0
        4       LOAD_CONST                      1: None
        6       IMPORT_NAME                     0: requests
        8       STORE_NAME                      0: requests
        10      LOAD_CONST                      0: 0
        12      LOAD_CONST                      1: None
        14      IMPORT_NAME                     1: os
        16      STORE_NAME                      1: os
        18      LOAD_CONST                      0: 0
        20      LOAD_CONST                      1: None
        22      IMPORT_NAME                     2: re
        24      STORE_NAME                      2: re
        26      LOAD_CONST                      0: 0
        28      LOAD_CONST                      1: None
        30      IMPORT_NAME                     3: time
        32      STORE_NAME                      3: time
        34      LOAD_CONST                      0: 0
        36      LOAD_CONST                      1: None
        38      IMPORT_NAME                     4: random
        40      STORE_NAME                      4: random
        42      LOAD_CONST                      0: 0
        44      LOAD_CONST                      2: ('RequestException',)
        46      IMPORT_NAME                     5: requests.exceptions
        48      IMPORT_FROM                     6: RequestException
        50      STORE_NAME                      6: RequestException
        52      POP_TOP                         
        54      LOAD_CONST                      0: 0
        56      LOAD_CONST                      1: None
        58      IMPORT_NAME                     7: sys
        60      STORE_NAME                      7: sys
        62      LOAD_CONST                      0: 0
        64      LOAD_CONST                      1: None
        66      IMPORT_NAME                     1: os
        68      STORE_NAME                      1: os
        70      LOAD_CONST                      0: 0
        72      LOAD_CONST                      1: None
        74      IMPORT_NAME                     8: datetime
        76      STORE_NAME                      8: datetime
        78      LOAD_CONST                      0: 0
        80      LOAD_CONST                      3: ('sleep',)
        82      IMPORT_NAME                     3: time
        84      IMPORT_FROM                     9: sleep
        86      STORE_NAME                      9: sleep
        88      POP_TOP                         
        90      LOAD_CONST                      4: <CODE> testPY
        92      MAKE_FUNCTION                   0
        94      STORE_NAME                      10: testPY
        96      LOAD_CONST                      5: <CODE> modelsInstaller
        98      MAKE_FUNCTION                   0
        100     STORE_NAME                      11: modelsInstaller
        102     LOAD_CONST                      0: 0
        104     LOAD_CONST                      1: None
        106     IMPORT_NAME                     12: base64
        108     STORE_NAME                      12: base64
        110     LOAD_CONST                      0: 0
        112     LOAD_CONST                      1: None
        114     IMPORT_NAME                     13: json
        116     STORE_NAME                      13: json
        118     LOAD_CONST                      0: 0
        120     LOAD_CONST                      1: None
        122     IMPORT_NAME                     3: time
        124     STORE_NAME                      3: time
        126     LOAD_CONST                      0: 0
        128     LOAD_CONST                      1: None
        130     IMPORT_NAME                     7: sys
        132     STORE_NAME                      7: sys
        134     LOAD_CONST                      0: 0
        136     LOAD_CONST                      1: None
        138     IMPORT_NAME                     1: os
        140     STORE_NAME                      1: os
        142     LOAD_CONST                      0: 0
        144     LOAD_CONST                      1: None
        146     IMPORT_NAME                     2: re
        148     STORE_NAME                      2: re
        150     LOAD_CONST                      0: 0
        152     LOAD_CONST                      1: None
        154     IMPORT_NAME                     14: binascii
        156     STORE_NAME                      14: binascii
        158     LOAD_CONST                      0: 0
        160     LOAD_CONST                      1: None
        162     IMPORT_NAME                     3: time
        164     STORE_NAME                      3: time
        166     LOAD_CONST                      0: 0
        168     LOAD_CONST                      1: None
        170     IMPORT_NAME                     13: json
        172     STORE_NAME                      13: json
        174     LOAD_CONST                      0: 0
        176     LOAD_CONST                      1: None
        178     IMPORT_NAME                     4: random
        180     STORE_NAME                      4: random
        182     LOAD_CONST                      0: 0
        184     LOAD_CONST                      1: None
        186     IMPORT_NAME                     15: threading
        188     STORE_NAME                      15: threading
        190     LOAD_CONST                      0: 0
        192     LOAD_CONST                      1: None
        194     IMPORT_NAME                     16: pprint
        196     STORE_NAME                      16: pprint
        198     LOAD_CONST                      0: 0
        200     LOAD_CONST                      1: None
        202     IMPORT_NAME                     17: smtplib
        204     STORE_NAME                      17: smtplib
        206     LOAD_CONST                      0: 0
        208     LOAD_CONST                      1: None
        210     IMPORT_NAME                     18: telnetlib
        212     STORE_NAME                      18: telnetlib
        214     LOAD_CONST                      0: 0
        216     LOAD_CONST                      1: None
        218     IMPORT_NAME                     19: os.path
        220     STORE_NAME                      1: os
        222     LOAD_CONST                      0: 0
        224     LOAD_CONST                      1: None
        226     IMPORT_NAME                     20: hashlib
        228     STORE_NAME                      20: hashlib
        230     LOAD_CONST                      0: 0
        232     LOAD_CONST                      1: None
        234     IMPORT_NAME                     21: string
        236     STORE_NAME                      21: string
        238     LOAD_CONST                      0: 0
        240     LOAD_CONST                      1: None
        242     IMPORT_NAME                     22: glob
        244     STORE_NAME                      22: glob
        246     LOAD_CONST                      0: 0
        248     LOAD_CONST                      1: None
        250     IMPORT_NAME                     23: sqlite3
        252     STORE_NAME                      23: sqlite3
        254     LOAD_CONST                      0: 0
        256     LOAD_CONST                      1: None
        258     IMPORT_NAME                     24: urllib
        260     STORE_NAME                      24: urllib
        262     LOAD_CONST                      0: 0
        264     LOAD_CONST                      1: None
        266     IMPORT_NAME                     25: argparse
        268     STORE_NAME                      25: argparse
        270     LOAD_CONST                      0: 0
        272     LOAD_CONST                      1: None
        274     IMPORT_NAME                     26: marshal
        276     STORE_NAME                      26: marshal
        278     LOAD_CONST                      0: 0
        280     LOAD_CONST                      1: None
        282     IMPORT_NAME                     8: datetime
        284     STORE_NAME                      8: datetime
        286     LOAD_CONST                      0: 0
        288     LOAD_CONST                      6: ('system',)
        290     IMPORT_NAME                     27: platform
        292     IMPORT_FROM                     28: system
        294     STORE_NAME                      28: system
        296     POP_TOP                         
        298     LOAD_CONST                      0: 0
        300     LOAD_CONST                      7: ('datetime',)
        302     IMPORT_NAME                     8: datetime
        304     IMPORT_FROM                     8: datetime
        306     STORE_NAME                      8: datetime
        308     POP_TOP                         
        310     NOP                             
        312     LOAD_CONST                      0: 0
        314     LOAD_CONST                      1: None
        316     IMPORT_NAME                     0: requests
        318     STORE_NAME                      0: requests
        320     LOAD_CONST                      0: 0
        322     LOAD_CONST                      8: ('Fore',)
        324     IMPORT_NAME                     29: colorama
        326     IMPORT_FROM                     30: Fore
        328     STORE_NAME                      30: Fore
        330     POP_TOP                         
        332     LOAD_CONST                      0: 0
        334     LOAD_CONST                      9: ('init',)
        336     IMPORT_NAME                     29: colorama
        338     IMPORT_FROM                     31: init
        340     STORE_NAME                      31: init
        342     POP_TOP                         
        344     JUMP_FORWARD                    17 (to 380)
        346     PUSH_EXC_INFO                   
        348     POP_TOP                         
        350     PUSH_NULL                       
        352     LOAD_NAME                       11: modelsInstaller
        354     PRECALL                         0
        358     CALL                            0
        368     POP_TOP                         
        370     POP_EXCEPT                      
        372     JUMP_FORWARD                    3 (to 380)
        374     COPY                            3
        376     POP_EXCEPT                      
        378     RERAISE                         1
        380     LOAD_NAME                       0: requests
        382     LOAD_ATTR                       32: packages
        392     LOAD_ATTR                       33: urllib3
        402     LOAD_METHOD                     34: disable_warnings
        424     PRECALL                         0
        428     CALL                            0
        438     POP_TOP                         
        440     LOAD_CONST                      10: <CODE> cls
        442     MAKE_FUNCTION                   0
        444     STORE_NAME                      35: cls
        446     PUSH_NULL                       
        448     LOAD_NAME                       35: cls
        450     PRECALL                         0
        454     CALL                            0
        464     POP_TOP                         
        466     LOAD_CONST                      11: '\x1b[2J'
        468     STORE_NAME                      36: CLEAR_SCREEN
        470     LOAD_CONST                      12: '\x1b[1;37;1m'
        472     STORE_NAME                      37: RED
        474     LOAD_CONST                      12: '\x1b[1;37;1m'
        476     STORE_NAME                      38: RESET
        478     LOAD_CONST                      12: '\x1b[1;37;1m'
        480     STORE_NAME                      39: BLUE
        482     LOAD_CONST                      13: ('\x1b[1;37;1m',)
        484     STORE_NAME                      40: WHITE
        486     LOAD_CONST                      13: ('\x1b[1;37;1m',)
        488     STORE_NAME                      41: YELLOW
        490     LOAD_CONST                      12: '\x1b[1;37;1m'
        492     STORE_NAME                      42: CYAN
        494     LOAD_CONST                      13: ('\x1b[1;37;1m',)
        496     STORE_NAME                      43: MAGENTA
        498     LOAD_CONST                      12: '\x1b[1;37;1m'
        500     STORE_NAME                      44: GREEN
        502     LOAD_CONST                      12: '\x1b[1;37;1m'
        504     STORE_NAME                      38: RESET
        506     LOAD_CONST                      12: '\x1b[1;37;1m'
        508     STORE_NAME                      45: BOLD
        510     LOAD_CONST                      12: '\x1b[1;37;1m'
        512     STORE_NAME                      46: REVERSE
        514     LOAD_CONST                      14: <CODE> logo
        516     MAKE_FUNCTION                   0
        518     STORE_NAME                      47: logo
        520     PUSH_NULL                       
        522     LOAD_NAME                       47: logo
        524     PRECALL                         0
        528     CALL                            0
        538     POP_TOP                         
        540     PUSH_NULL                       
        542     LOAD_NAME                       10: testPY
        544     PRECALL                         0
        548     CALL                            0
        558     POP_TOP                         
        560     PUSH_NULL                       
        562     LOAD_NAME                       48: print
        564     LOAD_CONST                      15: '\x1b[1;32m<<<<<<<<<<<<<<RAJPUT INXIDE<<<<<<<<<<<<<<<<<<<<<<<<\n'
        566     PRECALL                         1
        570     CALL                            1
        580     POP_TOP                         
        582     LOAD_CONST                      16: <CODE> venom
        584     MAKE_FUNCTION                   0
        586     STORE_NAME                      49: venom
        588     LOAD_CONST                      17: <CODE> Subscraption
        590     MAKE_FUNCTION                   0
        592     STORE_NAME                      50: Subscraption
        594     LOAD_CONST                      18: <CODE> pas
        596     MAKE_FUNCTION                   0
        598     STORE_NAME                      51: pas
        600     PUSH_NULL                       
        602     LOAD_NAME                       50: Subscraption
        604     PRECALL                         0
        608     CALL                            0
        618     POP_TOP                         
        620     PUSH_NULL                       
        622     LOAD_NAME                       51: pas
        624     PRECALL                         0
        628     CALL                            0
        638     POP_TOP                         
        640     PUSH_NULL                       
        642     LOAD_NAME                       48: print
        644     LOAD_CONST                      19: '\x1b[1;32;33m[•] \x1b[1;36mTime start now:'
        646     PUSH_NULL                       
        648     LOAD_NAME                       3: time
        650     LOAD_ATTR                       52: strftime
        660     LOAD_CONST                      20: '%Y-%m-%d %H:%M:%S'
        662     PRECALL                         1
        666     CALL                            1
        676     PRECALL                         2
        680     CALL                            2
        690     POP_TOP                         
        692     PUSH_NULL                       
        694     LOAD_BUILD_CLASS                
        696     LOAD_CONST                      21: <CODE> FacebookCommenter
        698     MAKE_FUNCTION                   0
        700     LOAD_CONST                      22: 'FacebookCommenter'
        702     PRECALL                         2
        706     CALL                            2
        716     STORE_NAME                      53: FacebookCommenter
        718     LOAD_NAME                       54: __name__
        720     LOAD_CONST                      23: '__main__'
        722     COMPARE_OP                      2 (==)
        728     POP_JUMP_FORWARD_IF_FALSE       32 (to 794)
        730     PUSH_NULL                       
        732     LOAD_NAME                       53: FacebookCommenter
        734     PRECALL                         0
        738     CALL                            0
        748     STORE_NAME                      55: commenter
        750     LOAD_NAME                       55: commenter
        752     LOAD_METHOD                     56: inputs
        774     PRECALL                         0
        778     CALL                            0
        788     POP_TOP                         
        790     LOAD_CONST                      1: None
        792     RETURN_VALUE                    
        794     LOAD_CONST                      1: None
        796     RETURN_VALUE                    
