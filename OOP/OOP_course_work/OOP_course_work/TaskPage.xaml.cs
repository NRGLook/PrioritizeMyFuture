using System;
using Microsoft.Maui.Controls;

namespace OOP_course_work
{
    public partial class TaskPage : ContentPage
    {
        private Bank _bankOfToday;

        public class Bank
        {
            private List<Task> _tasks;

            public Bank()
            {
                _tasks = new List<Task>();
            }

            public void AddTask(Task task)
            {
                _tasks.Add(task);
            }

            public void RemoveTask(Task task)
            {
                _tasks.Remove(task);
            }

            public List<Task> GetAllTasks()
            {
                return _tasks;
            }

            public void Clear()
            {
                _tasks.Clear();
            }
        }
        public TaskPage(Bank bankOfToday)
        {
            InitializeComponent();

            _bankOfToday = bankOfToday;
        }

        public TaskPage()
        {
        }

        private async void OnAddTaskClicked(object sender, EventArgs e)
        {
            if (string.IsNullOrWhiteSpace(TaskNameEntry.Text) || string.IsNullOrWhiteSpace(TaskTimeEntry.Text))
            {
                await DisplayAlert("Error", "Task name and time are required", "OK");
                return;
            }

            int taskTime;
            if (!int.TryParse(TaskTimeEntry.Text, out taskTime))
            {
                await DisplayAlert("Error", "Task time must be a valid number", "OK");
                return;
            }

       //     var task = new Task(TaskNameEntry.Text, taskTime, HashtagEntry.Text, "");

     //       _bankOfToday.AddTask(task);

            await Navigation.PopAsync();
        }
    }
}
