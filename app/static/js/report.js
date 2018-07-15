$(document).ready(function(){
    var dialog = $('#newBudget').get(0);
    dialogPolyfill.registerDialog(dialog);

    $('#newBudgetButton').click(function(){
        dialog.showModal();
    });

    $('#newBudgetClose').click(function(){
        dialog.close();
    });

    $('#newBudgetCreate').click(function(evt){
        evt.stopImmediatePropagation();
        var bName = $('#budgetName').val(),
            bAmount = $('#newAmount').val();
        var payload = {'name': bName, 'amount': bAmount};
        $.ajax({
                type : 'POST',
                url : '/budget/new',
                data: JSON.stringify(payload, null, '\t'),
                contentType: 'application/json;charset=UTF-8',
                success: function(result) {
                    dialog.close();
                }
            });
    });
});
