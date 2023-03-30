using System;
using Microsoft.Maui.Controls;

namespace OOP_course_work
{
    public partial class TaskPage : ContentPage
    {
        private Bank _bankOfToday;

        public class Bank
        {
            private int _totalTime;
            private List<Task> _tasks;

            public Bank(int defaultTime)
            {
                _totalTime = defaultTime;
                _tasks = new List<Task>();
            }

            public void AddTask(Task task)
            {
                _tasks.Add(task);
                _totalTime -= task.Time;
            }

            public int GetTotalTime()
            {
                return _totalTime;
            }
        }

        public class Task
        {
            public string Name { get; set; }
            public int Time { get; set; }
            public string Hashtag { get; set; }

            public Task(string name, int time, string hashtag)
            {
                Name = name;
                Time = time;
                Hashtag = hashtag;
            }
        }

        public TaskPage(Bank bankOfToday)
        {
            InitializeComponent();
            _bankOfToday = bankOfToday;
        }

        private async void AddTaskButton_Clicked(object sender, EventArgs e)
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

            var task = new Task(TaskNameEntry.Text, taskTime, HashtagEntry.Text);
            _bankOfToday.AddTask(task);

            await Navigation.PopAsync();
        }
    }
}
