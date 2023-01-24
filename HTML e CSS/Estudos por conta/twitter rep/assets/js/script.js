const tweeButton = document.querySelector('.cabecalho__menuItemTweetarButton');
const tweeButton2 = document.querySelector('.conteudoPrincipal__formularioButton');
const feed = document.querySelector('.conteudoPrincipal__listaTweets')

const textArea = document.querySelector('textarea');

tweeButton.addEventListener('click', tweetValueCatch);
tweeButton2.addEventListener('click', tweetValueCatch);

function tweetValueCatch(event){
    const tweetText = textArea.value;
    if(tweetText.length){tweetCreate(tweetText);}
    event.preventDefault();
}

function tweetCreate(tweetText){

    let data = new Date();
    let hora = data.getHours();
    let min = data.getMinutes();

    const tweet = {
        nome: "↣ Łucca",
        foto: "./assets/img/ProfilePic.png",
        usuario: " @lucca",
        texto: tweetText,
        tempo: `${hora}:${min}`
    }
    tweet_Template_List(tweet);
}

function tweet_Template_List(tweet){

    const {nome, foto, usuario, texto, tempo} = tweet

    let li = document.createElement("li");
    li.classList.add("conteudoPrincipal__tweet");

    let img = document.createElement("img");
    img.src = foto

    let div = document.createElement("div");
    div.classList.add("tweet__conteudo")

    let h2 = document.createElement("h2");
    h2.innerText = nome

    let span = document.createElement("span");
    span.innerText = `${usuario} ${tempo}`

    let p = document.createElement("p");
    p.innerText = texto


    li.appendChild(img);
    li.appendChild(div)

    div.appendChild(h2);
    div.appendChild(span);
    div.appendChild(p);
    
    feed.appendChild(li)

    textArea.value = ""
    
}
