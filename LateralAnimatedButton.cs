using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AnimatedButton
{
    public class LateralAnimatedButton : Button
    {
        
        Stopwatch sw = new Stopwatch();
        Timer Animation { get; set; } = new Timer();
        Timer AnimationBack { get; set; } = new Timer();
        public int AnimationInterval { get; set; } = 1; 
        public string CustomButtonText { get; set; } = ""; 
        public Color BackHoverColor { get; set; } = Color.Green;
        public Color TextHoverColor { get; set; } = Color.White; 
        public int BackgroundSpeed { get; set; } = 40;
        public double SmoothCorrectionFactor { get; set; } = 1.5F; 
        public bool UseSmoothSpeedIncrement { get; set; } = true; 
        private int incremental_x = 1;
        private bool DrawString = false;
        public LateralAnimatedButton()
        {
            
            this.SetStyle(System.Windows.Forms.ControlStyles.UserPaint |
                System.Windows.Forms.ControlStyles.AllPaintingInWmPaint |
                System.Windows.Forms.ControlStyles.OptimizedDoubleBuffer, true);
            //Events Section
            Animation.Interval = AnimationInterval;
            AnimationBack.Interval = AnimationInterval;
            Animation.Tick += ButtonAnimation;
            AnimationBack.Tick += ButtonAnimationBack;
            
            this.FlatStyle = FlatStyle.Flat;
            this.FlatAppearance.BorderSize = 0;
            this.BackColor = Color.FromArgb(240, 240, 240);//ligth grey
            this.ForeColor = Color.FromArgb(100, 100, 100);//dark grey
            this.Text = ""; //we want to override the standard text 
        }
       
        private void ButtonAnimationBack(object sender, EventArgs e)
        {
            if (UseSmoothSpeedIncrement)
            {
                incremental_x -= Convert.ToInt32(BackgroundSpeed * sw.Elapsed.TotalSeconds * SmoothCorrectionFactor);
            }
            else
            {
                incremental_x -= BackgroundSpeed;
            }
            if (incremental_x <= 0)
            {
                AnimationBack.Stop();
                incremental_x = 1;
            }
            this.Invalidate();
        }
        
        private void ButtonAnimation(object sender, EventArgs e)
        {
            if (UseSmoothSpeedIncrement)
            {
                incremental_x += Convert.ToInt32(BackgroundSpeed * sw.Elapsed.TotalSeconds * SmoothCorrectionFactor);
            }
            else
            {
                incremental_x += BackgroundSpeed;
            }
            if (incremental_x > this.Width * 3)
            {
                Animation.Stop();
            }
            this.Invalidate();
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            base.OnPaint(e);
            this.Text = "";
            var g = e.Graphics;
            g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
            if (incremental_x != 1) // 1 is the min value 
            {
                Rectangle r = new Rectangle(new Point(0 - incremental_x / 2, 0 - incremental_x / 2), new Size(incremental_x, this.Height + incremental_x));
                g.FillPie(new SolidBrush(BackHoverColor), r, 0, 360);
            }
            //redraw string
            StringFormat sf = new StringFormat();
            sf.LineAlignment = StringAlignment.Center;
            sf.Alignment = StringAlignment.Center;
            SolidBrush TextColor;
            if (DrawString)
                TextColor = new SolidBrush(TextHoverColor);
            else
                TextColor = new SolidBrush(this.ForeColor);

            g.DrawString(CustomButtonText, this.Font, TextColor, new Rectangle(new Point(0, 0), new Size(this.Width, this.Height)), sf);

            //done here!
        }

        protected override void OnMouseEnter(EventArgs e)
        {
            base.OnMouseEnter(e);
            DrawString = true;
            AnimationBack.Stop();
            Animation.Start();
            //Reset stopwatch
            sw.Reset();
            sw.Stop();
            sw.Start();
        }

        protected override void OnMouseLeave(EventArgs e)
        {
            base.OnMouseLeave(e);
            DrawString = false;
            Animation.Stop();
            AnimationBack.Start();
            //Reset stopwatch
            sw.Reset();
            sw.Stop();
            sw.Start();
        }
    }
}
