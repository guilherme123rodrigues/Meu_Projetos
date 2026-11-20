function clicar() {
    let nome = document.querySelector('#nome')
    let sobrenome = document.querySelector("#sobrenome")
    let email = document.querySelector("#e-mail")
    let endereco = document.querySelector("#endereço")
    let cep = document.querySelector("#cep")
    let sexo = document.getElementsByName('sexo')

    if (nome.value.length === 0 || sobrenome.value.length === 0 || email.value.length === 0 || endereco.value.length === 0 || cep.value.length === 0) {
        alert("ERRO! preencha os  campos")
    } else {
        
        /*if (sexo[0].checked) {
            alert(`Gênero: Musculino`)
        } else {
            alert(`Gênero: Feminino`)
        }*/
    }
}