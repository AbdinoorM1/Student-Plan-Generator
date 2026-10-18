# MaCS-Hacks-2026-Hackathon
Plan: To create a "Generate Student Plan" button on the existing Computer Science Acedemic Calendar page (Student Plan tab)
        -Frontend: Can do basic HTML, CSS, etc, or try using TypeScript if time allows
            -1 file:
                -Cloned the html on the Acedemic Calendar page and added a button to open up a modal in the existing webpage
                -Shows all courses across a 4-year timeline with checkboxes based on the stream selected

        -Backend: Python
            -Will need 2 files:
                -Web scraper (`web_scrape.py`): 
                    -can use requests/BeautifulSoup (new libraries for me, will need to look at docs)
                -Database ('sqlite.py'): 
                        -Used sqlite3 to create a table and store all comp sci courses and titles

                -Data Flow: 
                    -Scrapes data -> inputs to database -> references choices in modal -> calculates remaining requirements -> exports directly to an Excel sheet (.csv) with remaining credit info

