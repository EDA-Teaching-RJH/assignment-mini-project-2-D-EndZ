                          ┌──────────────────────────┐
                          │        START PROGRAM      │
                          └──────────────┬───────────┘
                                         │
                                         ▼
                          ┌──────────────────────────┐
                          │   Load CSV (if exists)   │
                          │   → init_database()       │
                          └──────────────┬───────────┘
                                         │
                                         ▼
                          ┌──────────────────────────┐
                          │     display_menu()        │
                          │  Ask for user full name   │
                          │  Show menu options        │
                          │  Return user choice       │
                          └──────────────┬───────────┘
                                         │
                                         ▼
                     ┌────────────────────────────────────────┐
                     │              USER CHOICE                │
                     └────────────────────────────────────────┘
                                         │
       ┌─────────────────────────────────┼──────────────────────────────────┐
       ▼                                 ▼                                  ▼

┌──────────────────────┐      ┌────────────────────────┐       ┌────────────────────────┐
│ 1. Add Account        │      │ 2. Generate Password   │       │ 3. List Accounts        │
│ add_account()         │      │ generate_and_add()     │       │ list_accounts()         │
│ • Ask website         │      │ • Ask website          │       │ • Loop through accounts │
│ • Ask username        │      │ • Ask username         │       │ • Print formatted table │
│ • Ask password        │      │ • Ask length           │       └────────────────────────┘
│ • Validate w/ regex   │      │ • Generate password    │
│ • Hash password       │      │ • Hash + save          │
│ • Save to list        │      │ • Show generated pwd   │
└──────────────────────┘      └────────────────────────┘

       │                                 │                                  │
       └─────────────────────────────────┼──────────────────────────────────┘
                                         │
                                         ▼

                     ┌────────────────────────────────────────┐
                     │ 4. Search Accounts                     │
                     │ search_accounts()                      │
                     │ • Ask for search term                  │
                     │ • Print matching accounts              │
                     └────────────────────────────────────────┘
                                         │
                                         ▼
                     ┌────────────────────────────────────────┐
                     │ 5. Remove Account                      │
                     │ remove_account()                       │
                     │ • Ask website + username               │
                     │ • Find matching account                │
                     │ • Remove from list                     │
                     └────────────────────────────────────────┘
                                         │
                                         ▼
                     ┌────────────────────────────────────────┐
                     │ 6. Save & Exit                         │
                     │ save_to_file()                         │
                     │ • Write all accounts to CSV            │
                     │ • Exit loop                            │
                     └────────────────────────────────────────┘
                                         │
                                         ▼
                          ┌──────────────────────────┐
                          │        END PROGRAM        │
                          └──────────────────────────┘
