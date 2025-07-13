import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { SvgPipe } from '../../pipes/svg/svg.pipe';
import { Router } from '@angular/router';

@Component({
  selector: 'app-new-group',
  standalone: true,
  imports: [FormsModule, CommonModule, SvgPipe],
  templateUrl: './new-group.component.html',
  styleUrl: './new-group.component.css'
})
export class NewGroupComponent {
  currentStep: number = 1;
  groupName: string = '';
  userName: string = '';

  constructor(private router: Router) { }

  nextStep() {
    this.currentStep++;

    if (this.currentStep === 3) {
      console.log('Group Name:', this.groupName);
      console.log('User Name:', this.userName);
      console.log('Group Created!');
      this.router.navigate(['/groups']);
    }
  }

  prevStep() {
    if (this.currentStep > 1) {
      this.currentStep--;
    }
  }

  canProceed(): boolean {
    if (this.currentStep === 1) {
      return this.groupName.trim().length > 0;
    } else if (this.currentStep === 2) {
      return this.userName.trim().length > 0;
    }
    return true;
  }
}
