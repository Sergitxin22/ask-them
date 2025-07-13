import { Component } from '@angular/core';
import { SvgPipe } from '../../pipes/svg/svg.pipe';
import { AsyncPipe } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-join',
  imports: [AsyncPipe, SvgPipe, FormsModule],
  templateUrl: './join.component.html',
  styleUrl: './join.component.css'
})
export class JoinComponent {
  groupID: string = '';

  joinGroup() {
    if (this.groupID.length > 0) {
      console.log('Id grupo: ' + this.groupID);
      return;
    }
  }

}
