$(document).ready(function(){
    var budgets = [];
    var dialog = $('#newBudget').get(0);
    dialogPolyfill.registerDialog(dialog);
    
    $.ajax({
        type : 'GET',
        url : '/budget/budgets',
        contentType: 'application/json;charset=UTF-8',
        success: function(result) {
            budgets = result;
            budgetChart(budgets);
            budgetDropdown(budgets);
        }
    });

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
                    budgets.push(payload);
                    budgetChart(budgets);
                    budgetDropdown(budgets);
                }
            });
    });

    function budgetDropdown(budgets) {
        $('#budgetList').html('');
        $('#budgetList').append('<option></option>');
        $.each(budgets, function(index, value){
            $('#budgetList').append(`<option value="${value.name}">${value.name}</option>`)
        });
    }
});
