import { Component, input, OnInit } from '@angular/core';

@Component({
  selector: 'app-vote-bar',
  imports: [],
  templateUrl: './vote-bar.component.html',
  styleUrl: './vote-bar.component.css'
})
export class VoteBarComponent implements OnInit {
  voteCount: number;

  constructor() {
    this.voteCount = 0;
  }

  ngOnInit() { }

  voteUp() {
    this.voteCount++;
  }

  voteDown() {
    this.voteCount--;
  }
}
