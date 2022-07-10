const nameList = {
    service1 : "Studium",
    service2 : "Arbeit",
    service3 : "Familie",
    service4 : "Freizeit",
    name: "Nazar El-Saifi",
    contactsite: "Kontakt",
    location: "Anfahrt",
    book: "Termin buchen",
    open: "Seite nicht für mobile Geräte geeignet!",
    read: "Termin buchen und mehr erfahren",
    text: "Hallo, ich heiße Nazar. Ich habe Spaß und gebe Gas. Die Seite hab ich aus Spaß erstellt. Du kannst aber wirklich hier ein Termin buchen",
    privacy: "Datenschutz",
    contact: "Kontakt",
    street: "Hand in Hand to",
    town: "696969 Wonderland",
    number: "0157/ 666666666 ",
    mail: "gehtDichNichtsAn@spaß.com",
    form1: "Vorname",
    form2: "Nachname",
    form3: "E-Mail Adresse",
    form4: "Thema",
    form5: "Abschicken",
    location2: "Sie können mich gut mit dem Auto, aber auch mit dem Bus Linie 69(Hand in Hand to Wonderland) erreichen. Bei Fragen einfach anrufen oder eine Mail schicken. "
}

for (element in nameList){
    try{
        document.querySelectorAll('.'+ element).forEach(i =>{
            i.innerHTML = nameList[element]
        })
    }
    catch(e){
        console.log(e)
    }
}



document.onload = ()=>{
    const table = document.getElementById('date_table');
    const trows = table.rows.length
    const tcol = table.rows[0].cells.length
    const date = document.getElementById('date_span')
    console.log(trows)
    console.log(tcol)
    for(i = 1; i< trows; i++ ){
        for(j = 0; j< tcol; j++){
            m = j
            k = i
            document.getElementById('date_table').rows[i].cells[j].childNodes[0].addEventListener('click',()=> {
                date.innerText = document.getElementById('date_table').rows[k].cells[m].firstChild.value
                console.log(document.getElementById('date_span').value)
            })
        }
    } 

}

try{
    document.getElementById('service_hinzufuegen').addEventListener('click', ()=>{
        document.querySelector('.disabled_form').setAttribute('class', 'service_hinzufuegen_form')
    })

}catch(e){

}


function parse_date(date){
    s = date.split(',')[2]
    console.log(s)
    return s
}


//date table transform
try{
    const table = document.getElementById('date_booking_table')
    rows = table.rows.length
    cols = table.rows[0].cells.length

    for(let i = 1; i< rows; i++){
        for(let j = 0; j < cols; j++){
            table.rows[i].cells[j].addEventListener('click', ()=>{
                td = document.querySelector('table').rows[i].cells[j]
                if(td.innerText == 'x'){
                    td.removeAttribute('data-href')
                }else{
                    location.href = td.getAttribute('data-href')
                }

            })
        }
    }

    for(let i = 1; i< rows; i++){
        for(let j = 0; j < cols; j++){
            td = table.rows[i].cells[j]
            if(td.innerText == 'x'){
                td.style.background = '#1f1f1f1f';
            }
        }
    }
    
}
catch(e){

}

try{
    enableTable("message_table")
    enableTable("booking_table")
    enableTable("service_overview_table")
}catch(e){

}


function enableTable(tableID){
    try{
        const table = document.getElementById(tableID)
        rows = table.rows.length
        cols = table.rows[0].cells.length

        for(let i = 1; i< rows; i++){
            const td = table.rows[i]
            td.addEventListener('click', ()=>{
                try{
                    const id = td.getAttribute('data-href')
                    document.getElementById(id).setAttribute('class', 'show_windos')
                }catch(e){
                }
            })
        }
    }catch(e){
    
    }
}


try{
    clickableTable("our_services_table")
    clickableTable("selected_services_table")
}catch(e){

}


function clickableTable(tableID){
    const table = document.getElementById(tableID)
    rows = table.rows.length
    cols = table.rows[0].cells.length
    for(let i = 1; i< rows; i++){
        for(let j = 0; j < cols; j++){
            table.rows[i].addEventListener('click', ()=>{
            tr = table.rows[i]
            location.href = tr.getAttribute('data-href')
            })
        }
    }
}
