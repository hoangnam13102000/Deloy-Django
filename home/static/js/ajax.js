// $(document).ready(function() {
//     $("a.top-bar-link").click(function() {
//         // alert(this.href);
//         var url = this.href;
//         $("main#kq").load(url);
//         return false;
//     })
// })

// $(document).ready(function() {
//     $("a.list-group-item").click(function() {
//         // alert(this.href);
//         var url = this.href;
//         $("main#kq").load(url);
//         return false;
//     })
// })

// $(document).ready(function() {
//     $('#comment-form').on('submit', function(e) {
//         e.preventDefault();
//         $.ajax({
//             type: 'POST',
//             url: this.href,
//             data: $(this).serialize(),
//             success: function(data) {
//                 if (data.status == 'success') {
//                     alert('Bình luận của bạn đã được gửi thành công!');
//                 } else {
//                     alert('Có lỗi xảy ra, vui lòng thử lại sau!');
//                 }
//             }
//         });
//     });
// });
// $(document).on('submit', '#comment-form', function(e) {
//     e.preventDefault();
//     $.ajax({
//         type: 'POST',
//         headers: { "X-CSRFToken": "{{ csrf_token }}" },
//         url: this.href,
//         data: $(this).serialize(),
//         success: function(data) {
//             if (data.success) {
//                 var comment = $('<div>').addClass('comment');
//                 var username = $('<span>').addClass('username').text(data.username + ':');
//                 var content = $('<span>').addClass('content').text(data.comment);
//                 comment.append(username, content);
//                 $('.comments-section').append(comment);
//                 $('#comment-form')[0].reset();
//             } else {
//                 alert(data.error);
//             }
//         }
//     });
// });