// Description: This function is used to add a word to the text area in the create_edit_pdf.html file.
function addWordToText(element) {
    let txtarea = document.getElementById("myTextarea");
    let wordToAdd;

    switch (element.textContent) {
        case "Firma":
            wordToAdd = element.getAttribute("name").toUpperCase();
            break;
        case "Adresa":
            wordToAdd = element.getAttribute("address").toUpperCase();
            break;
        case "Email":
            wordToAdd = element.getAttribute("email").toUpperCase();
            break;
        case "CUI":
            wordToAdd = element.getAttribute("cui").toUpperCase();
            break;
        case "Numar registru":
            wordToAdd = element.getAttribute("registerNumber").toUpperCase();
            break;
        case "Localitate":
            wordToAdd = element.getAttribute("city").toUpperCase();
            break;
        case "Contact":
            wordToAdd = element.getAttribute("contact").toUpperCase();
            break;
        case "Administrator":
            wordToAdd = element.getAttribute("manager").toUpperCase();
            break;
        case "Input Numar factura":
            wordToAdd = element.getAttribute("invoiceNumber");
            break;
        case "Input Data factura":
            wordToAdd = element.getAttribute("invoiceDate");
            break;    
        
    }
    txtarea.value = txtarea.value + " " + wordToAdd;
}