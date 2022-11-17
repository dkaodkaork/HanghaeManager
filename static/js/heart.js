const q_heart = document.querySelector('#q-heart');

q_heart.addEventListener('click', questHeartClick)

function questHeartClick(){
    console.log('this is heart');
    question_heart();
}
function answerHeartClick(id){
    console.log(id,'this is heart');
    answer_heart(id)
}


function question_heart() {
    $.ajax({
        type: "POST",
        url: "/heart/question",
        data: {
            quest_id : 8 ,
        },
        success: function (response) {
            console.log(response)
        }
    });
}

function answer_heart(id) {
    $.ajax({
        type: "POST",
        url: "/heart/answer",
        data: {
            answer_id : id ,
        },
        success: function (response) {
            console.log(response)
        }
    });
}
