$(document).ready(function () {
    show_rank();
    show_questions();
});

function show_rank() {
    $.ajax({
        type: 'GET',
        url: '/bulletin-board/rank',
        data: {},
        success: function (response) {
            let rows = response['ranks']
            for (let i = 0; i < rows.length; i++) {
                let user_name = rows[i]['user_name']
                let til_count = rows[i]['til_count']
                let rank = i + 1;

                let temp_html = `
                    <tr>
                        <td class="rank_num" ><a class="circle">${rank}등</a></td>
                        <td>${user_name}</td>
                        <td>${til_count} 포인트</td>
                    </tr>
                    `

                $('#ranking_list').append(temp_html)
            }
        }
    });
}

function show_questions() {
    $.ajax({
        type: 'GET',
        url: '/bulletin-board/questions',
        data: {},
        success: function (response) {
            let rows = response['quests']
            for (let i = 0; i < rows.length; i++) {

                let user_name = rows[i]['user_name']
                let question_id = rows[i]['question_id']
                let question_title = rows[i]['question_title']
                let question_date = rows[i]['question_date']
                let question_category = rows[i]['main_ability']
                let qestion_heart = rows[i]['q_heart_count']


                console.log(user_name, question_id, question_title, question_date)
                console.log(typeof question_date)
                let temp_html = `
                    <tr id="quest-list" class="quest-list ${question_category}" >
                        <td class="ability">${question_category}</td>  
                        <td class="title quest-title" >${question_title}</td>
                        <td class="author">${user_name}</td>
                        <td class="heart">❤️ ${qestion_heart}</td>
                    </tr>`
                $('#question_list').append(temp_html)
            }
        }
    });
}


{/* <button id="btn-all" class="category-btn"></button>
<button id="btn-react" class="category-btn"></button>
<button id="btn-node" class="category-btn"></button>
<button id="btn-spring" class="category-btn"></button> */}

// filtering
jQuery(function ($) {
    'use strict'
    /* 要素を取得(ボタンと要素) */
    let btnList = $('.btn-box *'),
        btnAll = $('#btn-all'),
        btnRed = $('#btn-react'),
        btnGreen = $('#btn-node'),
        btnBlue = $('#btn-spring');

    /* ボタンのいずれかをクリックした場合 */
    btnList.click(function () {
        if (!($(this).hasClass('is_active'))) {
            let filterClass = $(this).attr('key');
            btnList.removeClass('is_active');
            $(this).addClass('is_active');
            let box = $(".quest-list");

            box.each(function () {
                $(this).fadeOut(0);
                if ($(this).hasClass(filterClass)) {
                    $(this).stop().fadeIn(300);
                } else if (filterClass === 'all') {
                    box.stop().fadeIn(300);
                }
            });
        }
    });
});

jQuery(function ($) {
    'use strict'
    /* 要素を取得(ボタンと要素) */
    let btnList = $('.btn-box *'),
        btnAll = $('#btn-all'),
        btnRed = $('#btn-react'),
        btnGreen = $('#btn-node'),
        btnBlue = $('#btn-spring');

    /* ボタンのいずれかをクリックした場合 */
    btnList.click(function () {
        if (!($(this).hasClass('is_active'))) {
            let filterClass = $(this).attr('key');
            btnList.removeClass('is_active');
            $(this).addClass('is_active');
            let box = $(".quest-list");

            box.each(function () {
                $(this).fadeOut(0);
                if ($(this).hasClass(filterClass)) {
                    $(this).stop().fadeIn(300);
                } else if (filterClass === 'all') {
                    box.stop().fadeIn(300);
                }
            });
        }
    });
});

const searchForm = document.querySelector('#search-form')
const searchInput = document.querySelector('#search-form input');

function onSearchSubmit(event) {
    event.preventDefault();
    const keywords = searchInput.value;
    console.log(keywords)
    let list = $('.quest-list');
    searchInput.value = '';
    list.each(function () {
        $(this).fadeOut(0);
        if ($(this).text().indexOf(keywords) !== - 1) {
            $(this).stop().fadeIn(300);
            console.log($(this).text());
        }
    });
}

searchForm.addEventListener('submit', onSearchSubmit)

// btnList.click(function () {

//     if (!($(this).hasClass('is_active'))) {
//         let filterClass = $(this).attr('key');
//         btnList.removeClass('is_active');
//         $(this).addClass('is_active');


//         box.each(function () {
//             $(this).fadeOut(0);
//             if ($(this).hasClass(filterClass)) {
//                 $(this).stop().fadeIn(300);
//             } else if (filterClass === 'all') {
//                 box.stop().fadeIn(300);
//             }
//         });
//     }
// });