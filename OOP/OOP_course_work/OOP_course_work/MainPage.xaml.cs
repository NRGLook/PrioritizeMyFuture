using System;
using Microsoft.Maui.Controls;
using System.Collections.Generic;

namespace OOP_course_work
{
    public partial class MainPage : ContentPage
    {
        private TaskPage.Bank _bankOfToday;

        public MainPage()
        {
            InitializeComponent();
            _bankOfToday = new TaskPage.Bank(1440);
        }


        protected override void OnAppearing()
        {
            base.OnAppearing();
        }

        private async void AddTaskButton_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushAsync(new TaskPage(_bankOfToday));
        }

    }
}
