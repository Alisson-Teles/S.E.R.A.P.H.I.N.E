//get components for request
const button = document.getElementById("sendButton");
button.addEventListener('click', RequestSendFile);

function DesappearInput(){
    //get components
    const input = document.getElementById("input-file");
    const button = document.getElementById("sendButton");

    //makes visible  
    if(input.files.length > 0){
        input.classList.add("hidden");
        button.classList.remove("hidden");
    }
}

async function RequestSendFile(){
    
    const input = document.getElementById("input-file");
    const file = input.file[0];

   //if the file is not selected
    if(!file){
        alert("Selecione um arquivo antes de enviar!")
        return;
    }

    //buils the data to be sent
    const Data = new FormData();
    Data.append("file",file);

    //section that sends the request
    try{
        const response = await fetch("#rota",{
            method:"Post",
            body: Data
        });

        if(response.ok){
            const result = await response.json();
            console.log("Arquivo Enviado");
            alert("Arquivo enviado com sucesso");
        }else{
            console.error("Erro no envio do arquivo:",response.statusText);
            alert("Erro no envio.");
        }
    }catch(error){
        console.error("Erro na requisição:",error);
        alert("Erro na conexão com a API");
    }
}