let namesArray = ['Inderpreet', 
                        'Gauravjeet', 
            'Vigasdeep', 
            'Shaina', 
            'Hemant', 
            'Mandeep', 
            'Harry', 
            'Sahib', 
            'Manii', 
            'Nandini', 
            'Kamal', 
            'Rajvir'
        ];

        document.getElementById('cl').addEventListener('click', function(){
        let names = namesArray.sort();
  
        let randomName = names[Math.floor(Math.random() * names.length)];

        let res = document.getElementById('name');
        res.style.fontSize = '2.5em';
        res.innerHTML = randomName;

        $.ajax({
            url: 'sendName',
            type: 'POST',
            dataType: 'json',
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(randomName),
            success: function(response) {
              console.log(response);
            },
            error: function(error) {
              console.log(error);
            }
        })
        event.preventDefault();
        });