// Select comment edit buttons
const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

// Initialize the comment delete modal
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

// Modal initialization
const commentModal = new bootstrap.Modal(document.getElementById("commentModal"));
const modalTitle = document.getElementById("commentModalLabel");
const modalBody = document.getElementById("commentModalBody");
const modalConfirmButton = document.getElementById("commentModalConfirm");


// **EDIT COMMENT BUTTON LOGIC**
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id"); // Get the comment's ID
        let commentContent = document.getElementById(`comment${commentId}`).innerText; // Fetch comment text

        // Configure modal for editing
        modalTitle.innerText = "Edit Comment";
        modalBody.innerHTML = `
            <form id="commentEditForm" method="POST" action="/posts/${post_id}/edit_comment/${commentId}/">
                <textarea name="body" class="form-control" rows="3">${commentContent.trim()}</textarea>
                <input type="hidden" name="csrfmiddlewaretoken" value="${csrf_token}">
            </form>
        `;
        modalConfirmButton.innerText = "Update";
        modalConfirmButton.className = "btn btn-accept";

        // Attach the submit event to the button
        modalConfirmButton.onclick = () => {
            document.getElementById("commentEditForm").submit();
        };

        // Show the modal
        commentModal.show();
    });
}


// **DELETE COMMENT BUTTON LOGIC**
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id"); // Get the comment's ID
        deleteConfirm.href = `/posts/${post_id}/delete_comment/${commentId}/`; // Update delete URL

        // Show the modal
        deleteModal.show();
    });
}