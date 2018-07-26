$(document).ready(function(){
    var budgets = [];
    var lastBudgetId = 1;
    var dialogBudget = $('#newBudget').get(0);
    var dialogExpense = $('#newExpense').get(0);
    dialogPolyfill.registerDialog(dialogBudget);
    dialogPolyfill.registerDialog(dialogExpense);
    
    $.ajax({
        type : 'GET',
        url : '/budget/budgets',
        contentType: 'application/json;charset=UTF-8',
        success: function(result) {
            if (result.length > 0) { 
                budgets = result;
                barChart('budgets', budgets);
                budgetDropdown(budgets);
                lastBudgetId = budgets[budgets.length-1]
            }
        }
    });

    $('#newBudgetButton').click(function(){
        dialogBudget.showModal();
    });

    $('#newBudgetClose').click(function(){
        dialogBudget.close();
    });

    $('#newExpenseButton').click(function(){
        dialogExpense.showModal();
    });

    $('#newExpenseClose').click(function(){
        dialogExpense.close();
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
                    dialogBudget.close();
                    budgets.push(result);
                    barChart('budgets', budgets);
                    budgetDropdown(budgets);
                }
            });
    });

    $('#newExpenseCreate').click(function(evt){
        evt.stopImmediatePropagation();
        var bName = $('#expenseName').val(),
            bAmount = $('#newExpenseAmount').val(),
            budgetId = $('#budgetList').val();
        var payload = {'name': bName, 'amount': bAmount, 'budget_id': budgetId};
        $.ajax({
                type : 'POST',
                url : '/expense/new',
                data: JSON.stringify(payload, null, '\t'),
                contentType: 'application/json;charset=UTF-8',
                success: function(result) {
                    dialogExpense.close();
                }
            });
    });

    function budgetDropdown(budgets) {
        $('#budgetList').html('');
        $('#budgetList').append('<option></option>');
        $.each(budgets, function(index, value){
            $('#budgetList').append(`<option value="${value.id}">${value.name}</option>`)
        });
    }
});
