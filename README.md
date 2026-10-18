# MaCS-Hacks-2026-Hackathon
Plan: To create a "Generate Student Plan" button on the existing Computer Science Acedemic Calendar page
        -Frontend: Can do basic HTML, CSS, etc, or try using TypeScript if time allows
            -Potentially 1 file:
                -Depends on how I want to frame this:
                    -Can clone the html on the Acedemic Calendar page or simply add a button to open up a modal in the existing webpage

        -Backend: Python
            -Will need 3 files:
                -Web scraper: 
                    -can use requests/BeautifulSoup (new libraries for me, will need to look at docs)
                -Database: 
                    -can use sqlite to store the offered comp sci courses
                -generate_student_plan (main file): 
                    - calls web scraper (pre-loaded) > opens modal > asks 2 questions (what stream?, what year?) > references database > gives result (allows for export)

