using System.Runtime.CompilerServices;

namespace OOP_course_work
{
    public partial class MainPage : ContentPage
    {
        private double _bankOfToday = 1440;
        private double _bankOfTheFutureMe = 0;

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
        public double BankOfToday
        {
            get { return _bankOfToday; }
            set { SetProperty(ref _bankOfToday, value); }
        }

        public double BankOfTheFutureMe
        {
            get { return _bankOfTheFutureMe; }
            set { SetProperty(ref _bankOfTheFutureMe, value); }
        }

        public MainPage()
        {
            InitializeComponent();
            UpdateBankOfToday();
            var addTaskButton = new Button
            {
                Text = "Add Task",
                AutomationId = "addTaskButton"
            };

            addTaskButton.Clicked += async (sender, e) =>
            {
                await Navigation.PushAsync(new TaskPage());
            };


            Content = new StackLayout
            {
                Children = { addTaskButton }
            };
        }

        private void UpdateBankOfToday()
        {
            BankOfToday = _bankOfToday;
        }

        private void AddTask_Clicked(object sender, EventArgs e)
        {
            // TODO: Implement task adding functionality
        }
        protected bool SetProperty<T>(ref T backingStore, T value, [CallerMemberName] string propertyName = "", Action onChanged = null)
        {
            if (EqualityComparer<T>.Default.Equals(backingStore, value))
                return false;

            backingStore = value;
            onChanged?.Invoke();
            OnPropertyChanged(propertyName);

            return true;
        }

        private void OnAddTaskClicked(object sender, EventArgs e)
        {

        }
    }
}
