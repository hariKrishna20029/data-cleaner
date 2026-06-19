document.addEventListener("DOMContentLoaded", () => {
    const fileInput = document.querySelector("input[type=file]");
    
    fileInput.addEventListener("change" , () => {
        
        const file = fileInput.file[0];

        if(file){
            alert("Selected" + file.name);
        }

        }
    )
});