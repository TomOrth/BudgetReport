var dialog = document.getElementById('newBudget');
var showDialogButton = document.querySelector('#show-dialog');
if (! dialog.showModal) {
  dialogPolyfill.registerDialog(dialog);
}

function newBudgetDialog() {
    dialog.showModal()
}

function closeNewBudgetDialog(id) {
    dialog.close();
}